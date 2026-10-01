#!/usr/bin/env python3
"""One-command release verification for the public reproducibility package."""
from pathlib import Path
import argparse, hashlib, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST_SHA256.txt"
EXCLUDE = {"MANIFEST_SHA256.txt", "TEST_REPORT_v1.1.0.txt"}

def files_to_hash():
    return sorted(p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts and p.suffix != ".pyc" and p.relative_to(ROOT).as_posix() not in EXCLUDE)

def digest(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def write_manifest():
    lines=["# SHA-256 manifest for public release files (manifest and test report excluded)"]
    for p in files_to_hash():
        lines.append(f"{digest(p)}  {p.relative_to(ROOT).as_posix()}")
    MANIFEST.write_text("\n".join(lines)+"\n", encoding="utf-8", newline="\n")
    print(f"Wrote {MANIFEST.name} with {len(lines)-1} entries")

def check_manifest():
    if not MANIFEST.exists():
        raise SystemExit("Missing MANIFEST_SHA256.txt; run with --write-manifest")
    expected={}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"): continue
        sha, rel = line.split("  ",1); expected[rel]=sha
    actual={p.relative_to(ROOT).as_posix():digest(p) for p in files_to_hash()}
    if expected != actual:
        missing=sorted(set(expected)-set(actual)); extra=sorted(set(actual)-set(expected))
        changed=sorted(k for k in set(expected)&set(actual) if expected[k]!=actual[k])
        print("Manifest mismatch")
        if missing: print(" missing:", *missing, sep="\n  ")
        if extra: print(" extra:", *extra, sep="\n  ")
        if changed: print(" changed:", *changed, sep="\n  ")
        raise SystemExit(1)
    print(f"Manifest OK ({len(actual)} files)")

def run(rel):
    print(f"\n$ python3 {rel}", flush=True)
    p=subprocess.run([sys.executable, str(ROOT/rel)], cwd=ROOT, text=True)
    if p.returncode:
        raise SystemExit(p.returncode)

ap=argparse.ArgumentParser()
ap.add_argument("--write-manifest", action="store_true")
ap.add_argument("--skip-manifest", action="store_true")
args=ap.parse_args()
if args.write_manifest:
    write_manifest()
run("scripts/validate_events_v1_1_2.py")
run("scripts/test_mutations_v1_1_2.py")
run("scripts/analyze_public.py")
run("scripts/check_metadata.py")
if not args.skip_manifest:
    check_manifest()
print("\nRELEASE VERIFICATION: OK")
