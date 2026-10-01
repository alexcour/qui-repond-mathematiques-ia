# Codebook — public event corpus v1.1.2

The unit of analysis is a **claim-transition event**, not a conversation, file or AI model. Each event records an observable before/after change linked to a stable source identifier.

## Main identifiers

- `event_id`: unique event identifier.
- `case_id`: trajectory A, B, C or D.
- `claim_id`: stable claim identifier.
- `claim_parent_id` / `lineage_relation`: explicit lineage for restricted/transcribed child claims.
- `claim_version`: version label for the represented claim state.
- `source_id`: stable identifier into `data/sources_v1.1.2.csv`.

## Time and ordering

- `event_date`: ISO date.
- `date_granularity`: `day` or `interval`.
- `event_date_upper`: upper bound for interval events.
- `event_sequence`: within-day order where available.

## Four state axes

**Epistemic:** `NA`, `PROPOSED`, `DEMOTED`, `REFUTED`, `VERIFIED_LOCAL`, `OBSERVED`, `NOT_PROMOTED`, `CANDIDATE_UNIFORM`, `SCOPE_RESTRICTED`, `VERIFIED_FINITE`, `PROVED_UNREVIEWED`, `FALSE_AS_STATED`.

**Diffusion:** `NA`, `PRIVATE`, `PRIVATE_INTERNAL`, `PUBLIC`.

**Workflow:** `NA`, `PUBLICATION_PLANNED`, `BLOCKED`, `INTERNAL_RC`, `INTERNAL_CORRECTED`, `RELEASE_READY`, `RELEASED`, `HAL_READY`.

**Documentary / record status:** `NA`, `RECORDED`, `REPORTED_MISSING`, `REDERIVED`, `RESTORED_ANTERIORITY`, `WITHDRAWN_BY_CHANGELOG`, `REASSERTED_UNCITED`, `MISTRANSCRIBED`, `DETECTED_UNCORRECTED`, `QUALIFIED_TENDENCY`.

## Evidence state

`PRIMARY_PUBLIC`, `PRIMARY_INTERNAL`, `PRIMARY_PRIVATE_COPY`, `SECONDARY_PUBLIC`, `SECONDARY_INTERNAL`, `RAW_PRESENT_REPLAYED`.

Primary/secondary is relative to the documented act, not a global source-quality score. Any event-level override of a source default must contain an explicit `EVIDENCE_OVERRIDE:` justification.

## Source register and redaction

The source register records type, access class, date, analytical support, default evidence state and release eligibility. For private/internal sources, the locator is replaced by `NOT_REDISTRIBUTED::<source_id>`.

## Structural invariants

The validator checks unique identifiers, controlled vocabularies, source/access compatibility, dates, within-day ordering, lineage, actual axis changes, state chaining, claim-birth rules, evidence overrides, and the rule that publication/veto alone cannot alter epistemic status.

These are **structural consistency checks**, not mathematical validation of the underlying claims.
