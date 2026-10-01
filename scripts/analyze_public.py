#!/usr/bin/env python3
from pathlib import Path
import csv
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
with open(DATA / "events_v1.1.2.csv", encoding="utf-8-sig") as f:
    events = list(csv.DictReader(f))
with open(DATA / "sources_v1.1.2.csv", encoding="utf-8-sig") as f:
    sources = list(csv.DictReader(f))
claims = sorted({r["claim_id"] for r in events})
cases = Counter(r["case_id"] for r in events)
public_sources = sum(r["access"] == "PUBLIC" for r in sources)
print(f"events={len(events)}")
print(f"sources={len(sources)}")
print(f"claims={len(claims)}")
print("cases=" + ",".join(f"{k}:{cases[k]}" for k in sorted(cases)))
print(f"public_sources={public_sources}")
assert len(events) == 21
assert len(sources) == 13
assert len(claims) == 7
assert cases == Counter({"A": 5, "B": 3, "C": 7, "D": 6})
print("Public descriptive snapshot: OK")
