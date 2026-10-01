#!/usr/bin/env python3
"""Public-release gate, separate from local structural verification."""
from pathlib import Path
import json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/'scripts/check_metadata.py')],check=True)
c=json.loads((ROOT/'metadata/PUBLICATION_CONFIG.json').read_text(encoding='utf-8'))
failures=[]
if not re.fullmatch(r'https://hal[.]science/hal-[0-9]+(?:v[0-9]+)?',c.get('hal_url') or ''):
    failures.append('Actual HAL notice not entered.')
if not (c.get('hal_manuscript_license') or '').strip():
    failures.append("Author's manuscript licence decision not entered.")
if failures:
    print('PUBLIC RELEASE: PENDING')
    for m in failures:print('- '+m)
    raise SystemExit(2)
url=c['hal_url']
z=json.loads((ROOT/'.zenodo.json').read_text(encoding='utf-8'))
if not any(r.get('identifier')==url and r.get('relation')=='isSupplementTo' for r in z.get('related_identifiers',[])):
    raise SystemExit('PUBLIC RELEASE: metadata relation to HAL missing')
if url not in (ROOT/'README.md').read_text(encoding='utf-8') or url not in (ROOT/'CITATION.cff').read_text(encoding='utf-8'):
    raise SystemExit('PUBLIC RELEASE: HAL citation not propagated')
print('PUBLIC RELEASE METADATA: READY')
