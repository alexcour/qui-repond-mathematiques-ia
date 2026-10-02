# Couret-Unification: A Longitudinal Dataset of Claim-State Transitions in AI-Assisted Mathematical Research

Vetoes, Refutations, Scope Restrictions, Provenance Corrections, and Finite Verifications

Alexandre Couret · Independent researcher, France · ORCID 0009-0000-8246-7146

> Working Data Descriptor v0.3 · 1 October 2026. Describes frozen dataset v1.1.2. Distinct from the existing manuscript v1.1.1; no new release, submission or identifier is recorded.

## Abstract

We describe a longitudinal pilot dataset of mathematical claim-state transitions from the Couret-Unification research programme. The public snapshot contains 21 events involving seven claims and 13 registered sources across four selected trajectories. Each event records changes in epistemic, documentary, workflow or diffusion status, together with source access, evidence state, uncertainty and lineage. The records include human vetoes, non-promotion after a reported statistical test, scope restrictions, finite verification, refutation and provenance restoration. The release provides CSV tables, a codebook and Python checks for structural consistency and file integrity. Private source originals are not redistributed. The corpus is small, non-representative and partly reconstructed retrospectively; it does not estimate model reliability or causal effects of human–AI collaboration. It supports qualitative examination of claim histories and the development of provenance and annotation tools, subject to its source-access and validation limits.

## Background and Summary

The dataset records selected changes to mathematical claims during sustained research involving a human researcher and AI systems [1,2]. Its unit of observation is a source-linked transition. A final proof, publication or conversational answer is not treated as a substitute for the sequence of tests, restrictions and documentary corrections that preceded or followed it.

The observation unit differs from that of formal mathematics benchmarks. MiniF2F organises 488 formal problem statements across proof systems, whereas ProofNet contains 371 undergraduate mathematics examples combining formal statements with natural-language statements and proofs [3,4]. Process-supervision datasets operate at another level: PRM800K supplies step-level human feedback, and its associated experiments reported an advantage over outcome supervision on the studied MATH tasks [5]. Subsequent experiments identify sensitivities to annotation and evaluation procedures [6]. These results do not establish a training benefit for this small longitudinal corpus.

Provenance models and structured scientific assertions predate this dataset. PROV-O, micropublications and nanopublications provide established representations of provenance, claims and evidence [7–9]. This work documents a particular protocol–corpus combination, without claiming a new general provenance ontology or priority for preserving negative examples. The public release complements an existing working preprint [2] by exposing the event tables, coding rules and verification procedures.

## Methods

### Source selection and event construction

The release is a curated case series from one programme, not an exhaustive log of all interactions. It combines public repository documents, a contemporaneous private copy, internal reports and retrospective reconstructions. The public record does not establish a prospective sampling protocol or a complete denominator of candidate events. The four cases must therefore be treated as purposively selected, with historical source limitations retained in the event notes.

Each row identifies the claim, its scope and version, the supporting source, the recorded control and an explicit before/after change. A new child identifier preserves a restriction or transcription without silently changing the parent claim. Dates can be days or bounded intervals; event_sequence represents within-day order where available. Source dates and event dates remain separate. Some orderings are reconstructed from logical dependence and are qualified in the notes.

### Claim boundaries and four status dimensions

Documentary rules were introduced progressively to separate finite calculations, observations, conditional statements and candidate proofs from broader claims. The available evidence describes human vetoes, status files, release gates and structural checks. It does not show that every historical interaction used the same prompt-level constraints or that these rules caused a measurable improvement in model behaviour.

The schema separates four status dimensions. These are distinct fields with cross-field invariants, not statistically independent variables. The controlled labels belong to the axis defined in CODEBOOK.md; PROPOSED, DEMOTED, VERIFIED_LOCAL, OBSERVED and NOT_PROMOTED are epistemic labels, not workflow labels.

| Axis | Role | Examples from the codebook |
| --- | --- | --- |
| Epistemic | Recorded mathematical or empirical status | PROPOSED, REFUTED, VERIFIED_LOCAL, NOT_PROMOTED, SCOPE_RESTRICTED, VERIFIED_FINITE, PROVED_UNREVIEWED |
| Workflow | Editorial or release process | PUBLICATION_PLANNED, BLOCKED, INTERNAL_RC, INTERNAL_CORRECTED, RELEASE_READY, RELEASED, HAL_READY |
| Diffusion | Recorded visibility | PRIVATE, PRIVATE_INTERNAL, PUBLIC |
| Documentary or record | Condition of the claim record | RECORDED, REPORTED_MISSING, REDERIVED, RESTORED_ANTERIORITY, MISTRANSCRIBED, DETECTED_UNCORRECTED |

NA is also an allowed state where prescribed by the schema. The table lists examples rather than replacing the full controlled vocabularies. The field documentary_state describes how the event is documented; it is distinct from record_status_before and record_status_after. Source-relative evidence_state is also separate from the four before/after axes.

### Evidence status and limits of access

The source register assigns a default evidence state. The codebook distinguishes PRIMARY_PUBLIC, PRIMARY_INTERNAL, PRIMARY_PRIVATE_COPY, SECONDARY_PUBLIC, SECONDARY_INTERNAL and RAW_PRESENT_REPLAYED. An event-level override requires an EVIDENCE_OVERRIDE justification. Primary or secondary status concerns the documented act: a public changelog can be primary for a withdrawal but secondary for the earlier candidate that it reports.

Private conversations, email originals and complete internal reports are not redistributed. Non-public locators use NOT_REDISTRIBUTED::<source_id>; unnecessary private locators were reduced in free-text notes. These measures delimit the public representation without making the source originals accessible. They do not establish complete anonymisation or a general ethical-compliance finding. Unavailable originals, uncertain attribution and unreplayed historical calculations remain limitations of independent verification.

### Novelty and subsequent revisions

Mathematical validity and novelty are different questions. Identifying an established theorem does not make that theorem false. The v1.1.2 schema has no dedicated novelty_status field, and HOL2-C/D are not among its 21 events. Later HOL2 discussions may motivate source-linked events in a future version, but are not evidence of a novelty-refutation event in this snapshot. A proposed novelty axis is a future schema decision, not an implemented feature of v1.1.2.

## Data Records

The released object is the public reproducibility package [1]. Package v1.1.0, dataset v1.1.2 and existing manuscript v1.1.1 name different objects. The repository contains the following principal records. File paths are relative to its root.

| Record | Contents |
| --- | --- |
| data/events_v1.1.2.csv | UTF-8 CSV; transition records with 36 fields |
| data/sources_v1.1.2.csv | UTF-8 CSV; source register with 9 fields |
| CODEBOOK.md | Fields, controlled vocabularies and structural invariants |
| POSITIONING_AND_RELATED_WORK.md | Conceptual positioning; no implemented PROV-O or JSON-LD mapping is asserted |
| PUBLIC_SOURCE_BOUNDARY.md | Public representation and non-redistribution rules |
| POST_FREEZE_NOTES.md | Contextual or governance notes outside the frozen tables |
| CONTROL_DESIGN.md | Proposed future study design, not a completed control study |
| scripts/verify_release.py | Entry point orchestrating validators, mutation tests, descriptive checks and manifest verification |
| metadata/ and MANIFEST_SHA256.txt | Version settings, frozen-file fingerprints and public-file manifest |
| CITATION.cff and .zenodo.json | Citation and repository/archive metadata |

Join the two tables using source_id. Event records also contain event_id, case_id, claim_id, claim_parent_id, lineage_relation, dates, actor attribution, claim wording and scope, control descriptions, before/after states, uncertainty and notes. Blank optional values, NA, UNKNOWN and NOT_REDISTRIBUTED carry different meanings and should not be collapsed into a single missing-value category. The codebook and validator define the allowable values; observed frequencies do not define the schema.

Related mathematical artefacts retain their own releases and validation procedures. HOL-01 is a separate exact finite certificate at p=7 [10]. The pilot is not a bundled Lean project or a distribution of all finite-verification scripts, Barning–Hall certificates, private research reports or historical T1′–T4 material. The global T1′–T4 interpretation is superseded; this does not uniformly invalidate every historical component.

## Data Overview

The snapshot contains 21 events, seven claim identifiers and 13 source records. Encoded event dates run from 24 July 2025 to 28 September 2026; this is not continuous observation coverage. The source register contains three PUBLIC, nine PRIVATE_INTERNAL and one PRIVATE entry. Eleven source identifiers occur as event foreign keys; two additional source records provide supporting context. Actor-type annotations count 11 UNKNOWN, five HUMAN, three AI and two COLLECTIVE events, not participants.

| Case | Events | Recorded trajectory |
| --- | --- | --- |
| A | 5 | Universal arithmetic claim, veto, demotion/refutation; separate verified local child claim |
| B | 3 | Reported numerical alignment, non-promotion after a reported test and language restraint |
| C | 7 | Scope restriction, p=7 child certificate, public release and later documentary regression |
| D | 6 | Proof record, reported loss, rederivation, provenance restoration and a separate mistranscription |

## Technical Validation

The release verification command requires Python 3.10 or later and the standard library. It runs the structural validator, four mutation tests, the descriptive snapshot, metadata checks and SHA-256 manifest verification. On the checked snapshot it reports 517 structural checks passed and finishes with RELEASE VERIFICATION: OK. The mutation tests reject an ambiguous conversation identifier, an invalid initial claim state, an unjustified evidence override and an incorrect primary-source recoding.

```bash
python3 scripts/verify_release.py
```

The checks cover identifier uniqueness, controlled vocabularies, event-to-source references, dates, ordering, lineage, state chaining and prescribed axis rules. They confirm that event source references resolve; they do not require every supporting source record to be a direct event foreign key. Selected mutation tests demonstrate detection of those errors, not completeness of the validator or correctness of the mathematical claims.

Case C illustrates a cross-axis invariant. C1 and C2 concern C-UNIFORM, changing CANDIDATE_UNIFORM to SCOPE_RESTRICTED. C3 introduces the child C-P7 with epistemic_before=NA and epistemic_after=VERIFIED_FINITE. C4 subsequently changes its diffusion to PUBLIC while retaining VERIFIED_FINITE. Collapsing this lineage into a single chain ending in PUBLIC would mix claim identities and confuse publication with mathematical validation.

File hashes support byte comparisons against a recorded reference. They do not by themselves authenticate private originals, establish real-world event dates or show that the history is complete. The frozen data and validator fingerprints are recorded separately from current metadata. The original v1.1.0 tag is preserved, including its state before DOI insertion into the main branch.

Independent blinded recoding and inter-annotator agreement are not established by this release. Historical case-B measurements were not replayed by these structural checks. External mathematical proofs require their own evidence and verification. Successful checks therefore support technical consistency of the public representation, with the semantic and historical limits stated above.

## Usage Notes

Record the selected archive or commit, run the verifier and read the codebook before analysis. Preserve claim lineage, date intervals and source-access qualifications. For a documented main-branch snapshot containing the current identifiers, the following commands reproduce the checked reference. The commit is not relabelled as the original archived tag.

```bash
git clone https://github.com/alexcour/qui-repond-mathematiques-ia.git
cd qui-repond-mathematiques-ia
git checkout b15eb057dcea32b8290961bdaa22909324f4aa17
python3 scripts/verify_release.py
```

The records may serve as a small fixture for checking provenance software or an independently designed annotation exercise. They are not an independently adjudicated gold-standard transcript benchmark: full source conversations are not provided and the labels have not been externally validated as such. A classifier evaluation would require an explicit target, a justified input representation, independent label review and a declared policy for restricted sources.

Events within the same claim and case are dependent. A random row split can leak related trajectory information into both training and evaluation. Any exploratory task should preserve claim or case groups where possible and report its very small effective sample. This one-program pilot cannot estimate population-level AI reliability, compare model families or establish causal benefits. It is not a demonstrated training resource for process reward models.

Corrections and extensions should be versioned with a source and rationale. Later proof, novelty and provenance events should not be inserted retrospectively into the frozen v1.1.2 tables. A result classified as classical must remain distinct from a mathematically refuted assertion.

## Data Availability

The event and source tables are publicly available in https://github.com/alexcour/qui-repond-mathematiques-ia and the package archive identified by version DOI https://doi.org/10.5281/zenodo.23079572 [1]. The series DOI is https://doi.org/10.5281/zenodo.23079571. The associated existing manuscript is https://hal.science/hal-05773424 [2]. These identifiers describe the existing objects, not a new Data Descriptor deposit. Private source originals are not redistributed and access to them is not promised.

## Code Availability

The same repository provides the structural validator, mutation scripts, descriptive audit and release checks. The public code, CSV exports and repository documentation, including CODEBOOK.md, retain the MIT License. The associated existing narrative manuscript is recorded under CC-BY 4.0. This draft does not change these licences or assign rights to private or third-party originals. The verification pipeline uses Python 3.10 or later with the standard library; it does not require a bundled Lean, SageMath or PARI/GP environment.

## References

1. Couret, A. Qui répond des mathématiques produites par machine ? Public reproducibility package v1.1.0, frozen dataset v1.1.2 (2026). https://doi.org/10.5281/zenodo.23079572

2. Couret, A. Qui répond des mathématiques produites par machine ? Traçabilité longitudinale des transitions de revendications en recherche mathématique assistée par IA. Working preprint, internal v1.1.1 (2026). https://hal.science/hal-05773424

3. Zheng, K., Han, J. M. & Polu, S. MiniF2F: a cross-system benchmark for formal Olympiad-level mathematics. ICLR 2022; arXiv:2109.00110v2. https://arxiv.org/abs/2109.00110v2

4. Azerbayev, Z. et al. ProofNet: Autoformalizing and Formally Proving Undergraduate-Level Mathematics. Preprint, arXiv:2302.12433 (2023). https://arxiv.org/abs/2302.12433

5. Lightman, H. et al. Let’s Verify Step by Step. arXiv:2305.20050 (2023). PRM800K data are described in this paper. https://arxiv.org/abs/2305.20050

6. Zhang, Z. et al. The Lessons of Developing Process Reward Models in Mathematical Reasoning. Findings of ACL 2025, 10495–10516 (2025). https://doi.org/10.18653/v1/2025.findings-acl.547

7. Lebo, T., Sahoo, S. & McGuinness, D. (eds). PROV-O: The PROV Ontology. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/

8. Clark, T., Ciccarese, P. N. & Goble, C. A. Micropublications: a semantic model for claims, evidence, arguments and annotations in biomedical communications. Journal of Biomedical Semantics 5, 28 (2014). https://doi.org/10.1186/2041-1480-5-28

9. Nanopublication Guidelines. Working draft, consulted 1 October 2026. https://nanopub.net/guidelines/working_draft/

10. Couret, A. HOL-01 exact finite monodromy certificate at p=7, version 1.1.1 (2026). https://doi.org/10.5281/zenodo.22978389

## Author Contributions

> **Pre-submission placeholder — author input required.** Do not infer contributions from repository history. Complete the author-contribution declaration in the active Scientific Data submission workflow; retain a manuscript statement only if the submission system in use requires it.

## Competing Interests

> **Pre-submission placeholder — author declaration required.** No competing-interest declaration is inferred from public repository contents. Complete the declaration in the active Scientific Data submission workflow; add manuscript text only if the submission system in use requires it.

## Funding

> **Pre-submission placeholder — author declaration required.** No funding source, grant, or absence of external funding is inferred from public repository contents. Replace this placeholder with the author's accurate funding statement before submission.
