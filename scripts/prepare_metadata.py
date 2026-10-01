#!/usr/bin/env python3
"""Enter genuine identifiers and rights choices; never edits frozen data."""
from pathlib import Path
import argparse,datetime,json,re
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser()
ap.add_argument('--hal-url',required=True)
ap.add_argument('--hal-license',required=True,help="Actual author decision, e.g. the licence chosen in HAL; no default")
ap.add_argument('--release-date',default=None,help='Actual release date, YYYY-MM-DD')
ap.add_argument('--zenodo-version-doi')
ap.add_argument('--zenodo-concept-doi')
a=ap.parse_args()
if not re.fullmatch(r'https://hal[.]science/hal-[0-9]+(?:v[0-9]+)?',a.hal_url):ap.error('Use the actual https://hal.science/hal-... notice URL')
if re.search(r'[\r\n]',a.hal_license) or not a.hal_license.strip():ap.error('One nonempty line for the actual licence decision')
cfg=json.loads((ROOT/'metadata/PUBLICATION_CONFIG.json').read_text())
date=a.release_date or cfg['publication_date']
datetime.date.fromisoformat(date)
for doi in (a.zenodo_version_doi,a.zenodo_concept_doi):
    if doi and not re.fullmatch(r'10[.]5281/zenodo[.][0-9]+',doi):ap.error('Use a genuine Zenodo DOI, without URL prefix')
previous=cfg.get('hal_url')
cfg.update(hal_url=a.hal_url,hal_manuscript_license=a.hal_license.strip(),publication_date=date)
if a.zenodo_version_doi:cfg['zenodo_version_doi']=a.zenodo_version_doi
if a.zenodo_concept_doi:cfg['zenodo_concept_doi']=a.zenodo_concept_doi
z=json.loads((ROOT/'.zenodo.json').read_text());z['publication_date']=date
rel=[r for r in z.get('related_identifiers',[]) if r.get('relation')!='isSupplementTo']
rel.append({'identifier':a.hal_url,'relation':'isSupplementTo','scheme':'url'})
z['related_identifiers']=rel
cff=(ROOT/'CITATION.cff').read_text()
cff=re.sub(r'^date-released:.*$', 'date-released: '+date,cff,flags=re.M)
cff=re.sub(r'^  url: "https://hal\.science/hal-[^"]+"\n','',cff,flags=re.M)
cff=cff.rstrip()+'\n  url: "'+a.hal_url+'"\n'
if a.zenodo_version_doi:
    cff=re.sub(r'^doi:.*\n','',cff,flags=re.M)
    cff='doi: "'+a.zenodo_version_doi+'"\n'+cff
readme=(ROOT/'README.md').read_text()
readme=re.sub(r'^- HAL record:.*$', '- HAL record: '+a.hal_url,readme,flags=re.M)
if a.zenodo_version_doi:readme=re.sub(r'^- Zenodo DOI:.*$', '- Zenodo DOI: https://doi.org/'+a.zenodo_version_doi,readme,flags=re.M)
meta=(ROOT/'metadata/HAL_METADATA.txt').read_text()
meta=re.sub(r'(NOTICE HAL\n)[^\n]*',lambda m:m[1]+a.hal_url,meta)
meta=re.sub(r'(LICENCE DU MANUSCRIT\n)[^\n]*',lambda m:m[1]+a.hal_license.strip(),meta)
for path,payload in [('metadata/PUBLICATION_CONFIG.json',json.dumps(cfg,ensure_ascii=False,indent=2)),('.zenodo.json',json.dumps(z,ensure_ascii=False,indent=2)),('CITATION.cff',cff),('README.md',readme),('metadata/HAL_METADATA.txt',meta)]:
    (ROOT/path).write_text(payload.rstrip()+'\n',encoding='utf-8')
print('Actual metadata entered. Regenerate manifest and test report, then run check_release_ready.py.')
