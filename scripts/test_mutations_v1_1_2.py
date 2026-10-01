#!/usr/bin/env python3
"""Mutation tests for validator v1.1.2. Every mutation must be rejected."""
from pathlib import Path
import csv, shutil, subprocess, tempfile, sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
BASE_E = DATA / "events_v1.1.2.csv"
BASE_S = DATA / "sources_v1.1.2.csv"
VAL = ROOT / "scripts" / "validate_events_v1_1_2.py"

def run_case(name, mutate):
    with tempfile.TemporaryDirectory() as td_raw:
        td = Path(td_raw)
        (td / "data").mkdir(); (td / "scripts").mkdir()
        e = td / "data" / "events_v1.1.2.csv"
        s = td / "data" / "sources_v1.1.2.csv"
        v = td / "scripts" / "validate_events_v1_1_2.py"
        shutil.copy(BASE_E, e); shutil.copy(BASE_S, s); shutil.copy(VAL, v)
        rows = list(csv.DictReader(open(e, encoding="utf-8-sig")))
        fields = rows[0].keys()
        mutate(rows)
        with open(e, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
        p = subprocess.run([sys.executable, str(v)], cwd=td, text=True, capture_output=True)
        if p.returncode == 0:
            raise SystemExit(f"MUTATION NOT DETECTED: {name}")
        last = (p.stdout.strip().splitlines() or p.stderr.strip().splitlines() or ["rejected"])[-1]
        print(f"OK mutation rejected: {name} -> {last}")

rows = list(csv.DictReader(open(BASE_E, encoding="utf-8-sig")))
c1 = next(r for r in rows if r["event_id"] == "C1")
assert c1["evidence_state"] == "SECONDARY_PUBLIC"
print("OK baseline C1 = SECONDARY_PUBLIC")

def m_conv(rows):
    next(r for r in rows if r["event_id"] == "A2")["uncertainty"] = "Primary conversation C5 not recovered."
run_case("ambiguous conversation identifier", m_conv)

def m_birth(rows):
    next(r for r in rows if r["event_id"] == "B1")["epistemic_before"] = "PROPOSED"
run_case("first claim event starts with before != NA", m_birth)

def m_override(rows):
    r = next(r for r in rows if r["event_id"] == "D4")
    r["notes"] = "Keep domain s >= 1."
run_case("evidence override without justification", m_override)

def m_c1(rows):
    r = next(r for r in rows if r["event_id"] == "C1")
    r["evidence_state"] = "PRIMARY_PUBLIC"; r["notes"] = ""
run_case("C1 incorrectly recoded as PRIMARY_PUBLIC", m_c1)

print("All expected mutations were detected.")
