#!/usr/bin/env python3
"""Check documentary metadata and preserved frozen bytes; no scientific proof claim."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
def check(ok,msg):
    if not ok: raise SystemExit('METADATA FAIL: '+msg)
cfg=json.loads((ROOT/'metadata/PUBLICATION_CONFIG.json').read_text(encoding='utf-8'))
z=json.loads((ROOT/'.zenodo.json').read_text(encoding='utf-8'))
cff=(ROOT/'CITATION.cff').read_text(encoding='utf-8')
version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
check(version==cfg['package_version']==z['version'],'package versions agree')
check(re.search(r'^version: '+re.escape(version)+r'$',cff,re.M) is not None,'CFF version')
check(z['publication_date']==cfg['publication_date'],'release dates agree')
check('date-released: '+cfg['publication_date'] in cff,'CFF date')
check(cfg['manuscript_version']=='1.1.1' and cfg['dataset_version']=='1.1.2','separate manuscript and dataset versions')
check(z['license']=='mit' and 'license: MIT' in cff,'existing public MIT licence retained')
check(z['creators'][0]['orcid']=='0009-0000-8246-7146','retained author ORCID')
f=json.loads((ROOT/'metadata/FROZEN_SNAPSHOT_SHA256.json').read_text(encoding='utf-8'))
for rel,expected in f.items():
    check(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==expected,'frozen bytes '+rel)
check('doi: "'+cfg['zenodo_version_doi']+'"' in cff,'package DOI retained in CFF')
if cfg.get('hal_submission_status')=='rejected':
    historical=cfg['hal_submission_url']
    check(cfg.get('hal_url') is None,'rejected submission is not an active HAL record')
    check(cfg.get('manuscript_url')!=historical,'rejected submission is not a public manuscript URL')
    check(not any(r.get('identifier')==historical for r in z.get('related_identifiers',[])),
          'rejected HAL submission removed from active archive relations')
    check(historical not in cff and 'associated HAL preprint' not in cff,
          'package citation does not redirect to rejected HAL submission')
    check('preferred-citation:' not in cff,'package remains the preferred citation')
print('Metadata versions and frozen bytes: OK')
