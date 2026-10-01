#!/usr/bin/env python3
"""Structural validator for the public v1.1.2 claim-transition snapshot."""
from pathlib import Path
import csv, re, sys
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
E = list(csv.DictReader(open(DATA / "events_v1.1.2.csv", encoding="utf-8-sig")))
_SROWS = list(csv.DictReader(open(DATA / "sources_v1.1.2.csv", encoding="utf-8-sig")))
S = {r["source_id"]: r for r in _SROWS}
n = 0

def check(c, msg):
    global n
    n += 1
    if not c:
        print("FAIL", msg)
        sys.exit(1)

V = {
 "epistemic": {"NA","PROPOSED","DEMOTED","REFUTED","VERIFIED_LOCAL","OBSERVED","NOT_PROMOTED","CANDIDATE_UNIFORM",
               "SCOPE_RESTRICTED","VERIFIED_FINITE","PROVED_UNREVIEWED","FALSE_AS_STATED"},
 "diffusion": {"NA","PRIVATE","PRIVATE_INTERNAL","PUBLIC"},
 "workflow": {"NA","PUBLICATION_PLANNED","BLOCKED","INTERNAL_RC","INTERNAL_CORRECTED","RELEASE_READY","RELEASED","HAL_READY"},
 "record_status": {"NA","RECORDED","REPORTED_MISSING","REDERIVED","RESTORED_ANTERIORITY","WITHDRAWN_BY_CHANGELOG",
                   "REASSERTED_UNCITED","MISTRANSCRIBED","DETECTED_UNCORRECTED","QUALIFIED_TENDENCY"},
}
LINEAGE = {"", "SPLIT_FROM", "TRANSCRIPTION_OF"}
EVIDENCE = {"PRIMARY_PUBLIC","PRIMARY_INTERNAL","PRIMARY_PRIVATE_COPY","SECONDARY_PUBLIC","SECONDARY_INTERNAL","RAW_PRESENT_REPLAYED"}
SOURCE_ACCESS = {"PUBLIC","PRIVATE_INTERNAL","PRIVATE"}
PUBLIC_RELEASE = {"YES","NO","REDACTED_ONLY","YES_IF_PACKAGED","YES_AFTER_MANUAL_METADATA_CHECK"}
claims = {r["claim_id"] for r in E}
check(len({r["event_id"] for r in E}) == len(E), "event_id unique")
check(len(S) == len(_SROWS), "source_id unique")
_c1 = next((r for r in E if r["event_id"] == "C1"), None)
check(_c1 is not None and _c1["evidence_state"] == "SECONDARY_PUBLIC", "C1 must remain SECONDARY_PUBLIC")
for src in _SROWS:
    check(src["access"] in SOURCE_ACCESS, f"{src['source_id']} known source access")
    check(src["evidence_state_default"] in EVIDENCE, f"{src['source_id']} known default evidence state")
    check(src["public_release_ok"] in PUBLIC_RELEASE, f"{src['source_id']} known release flag")
    if src["date"]:
        check(re.fullmatch(r"\d{4}-\d{2}-\d{2}", src["date"]) is not None, f"{src['source_id']} ISO source date")
seq = defaultdict(set)
for r in E:
    i = r["event_id"]
    check(r["source_id"] in S, f"{i} known source")
    check(r["source_access"] == S[r["source_id"]]["access"], f"{i} event/source access match")
    check(r["evidence_state"] in EVIDENCE, f"{i} known evidence_state")
    text_blob = " ".join(r.get(k, "") for k in ("control_description","uncertainty","notes","claim_short"))
    check(re.search(r"\bconversation C[1-9]\b", text_blob, flags=re.I) is None, f"{i} ambiguous conversation id; use CONV-Cx")
    check(re.search(r"\breported in C[1-9]\b", text_blob, flags=re.I) is None, f"{i} ambiguous reported-in id; use CONV-Cx")
    if r["evidence_state"] != S[r["source_id"]]["evidence_state_default"]:
        check("EVIDENCE_OVERRIDE:" in r["notes"], f"{i} evidence override without justification")
    for ax in V:
        for side in ("before", "after"):
            check(r[f"{ax}_{side}"] in V[ax], f"{i} {ax}_{side} controlled vocabulary")
    check(r["lineage_relation"] in LINEAGE, f"{i} known lineage")
    check(bool(r["claim_parent_id"]) == bool(r["lineage_relation"]), f"{i} parent iff lineage")
    if r["claim_parent_id"]:
        check(r["claim_parent_id"] in claims, f"{i} parent exists")
    check(re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["event_date"]) is not None, f"{i} ISO event date")
    if r["date_granularity"] == "interval":
        check(r["event_date_upper"] > r["event_date"] and r["event_sequence"] == "", f"{i} well-formed interval")
    else:
        check(r["event_date_upper"] == "" and r["event_sequence"].isdigit(), f"{i} integer day sequence")
        seq[(r["event_date"], r["event_sequence"])].add(r["source_id"])
    moved = [ax.upper() if ax != "record_status" else "DOCUMENTARY" for ax in V if r[f"{ax}_before"] != r[f"{ax}_after"]]
    declared = r["transition_axis"].split("|")
    check(declared == (moved or ["NONE"]), f"{i} declared axis equals actual changes")
    check(bool(moved), f"{i} carries at least one transition")
    if r["actor_role"] in {"publish", "veto"}:
        check(r["epistemic_before"] == r["epistemic_after"], f"{i} publication/veto does not alter epistemic status")
for k, srcs in seq.items():
    check(len(srcs) == 1, f"same date/sequence only within same source act: {k}")
by = defaultdict(list)
for r in E:
    by[r["claim_id"]].append(r)
for c, rs in by.items():
    rs_birth = sorted(rs, key=lambda r: (r["event_date"], int(r["event_sequence"]) if r["event_sequence"] else 10**6))
    check(rs_birth[0]["epistemic_before"] == "NA", f"{c} first event begins at epistemic NA")
    keys = [(r["event_date"], r["event_sequence"]) for r in rs if r["event_sequence"]]
    check(len(keys) == len(set(keys)), f"{c} no duplicate claim position")
    rs.sort(key=lambda r: (r["event_date"], int(r["event_sequence"]) if r["event_sequence"] else 10**6))
    for a, b in zip(rs, rs[1:]):
        if a["date_granularity"] == "interval":
            check(a["event_date_upper"] >= b["event_date"], f"{c} interval upper bound compatible with next event")
        for ax in ("epistemic", "record_status"):
            if b[f"{ax}_before"] != "NA":
                check(a[f"{ax}_after"] == b[f"{ax}_before"], f"{c} {ax} state chaining {a['event_id']}->{b['event_id']}")
print(f"{n} structural checks passed - exit 0.")
