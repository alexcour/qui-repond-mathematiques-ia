#!/usr/bin/env python3
"""Local documentary gate; no network audit, submission or publication."""
from pathlib import Path
import argparse,json,subprocess,sys
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser()
ap.add_argument('--documentation-only',action='store_true',
    help='Check current documentation only; does not attest publication readiness')
a=ap.parse_args()
subprocess.run([sys.executable,str(ROOT/'scripts/check_metadata.py')],check=True)
c=json.loads((ROOT/'metadata/PUBLICATION_CONFIG.json').read_text(encoding='utf-8'))
if a.documentation_only:
    print('DOCUMENTATION METADATA: CONSISTENT (local checks only; no new release authorized)')
    raise SystemExit(0)
url=c.get('manuscript_url') or ''
parts=urlsplit(url)
failures=[]
if parts.scheme!='https' or not parts.netloc or c.get('manuscript_archive_status')!='published_verified':
    failures.append('Public manuscript archive not verified; a submission identifier is insufficient.')
if not (c.get('manuscript_license') or '').strip():
    failures.append("Author's manuscript licence decision not entered.")
if failures:
    print('PUBLIC RELEASE: PENDING (does not withdraw an already published package)')
    for m in failures: print('- '+m)
    raise SystemExit(2)
z=json.loads((ROOT/'.zenodo.json').read_text(encoding='utf-8'))
if not any(r.get('identifier')==url and r.get('relation')=='isSupplementTo' for r in z.get('related_identifiers',[])):
    raise SystemExit('PUBLIC RELEASE: verified manuscript relation missing')
if url not in (ROOT/'README.md').read_text(encoding='utf-8'):
    raise SystemExit('PUBLIC RELEASE: verified manuscript URL not documented')
print('PUBLIC RELEASE METADATA: CONSISTENT (operator-recorded verification; no live audit)')
