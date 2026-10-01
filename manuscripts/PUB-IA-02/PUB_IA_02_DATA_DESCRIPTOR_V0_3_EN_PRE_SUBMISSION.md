# Longitudinal claim-state transitions in AI-assisted mathematical research

> **DRAFT / candidate Data Descriptor.** This manuscript describes the frozen public dataset v1.1.2. It is not a new dataset release, does not alter the frozen CSV snapshot, and does not create a new DOI or HAL record.

**Alexandre Couret**

Independent researcher, France \| ORCID 0009-0000-8246-7146

Data Descriptor manuscript

# Abstract

AI-assisted mathematical research can produce claims whose evidential
status changes as they are tested, restricted, verified, refuted,
documented, or released. This Data Descriptor presents a frozen
longitudinal case-study dataset that records such changes as
source-linked claim-transition events. Version 1.1.2 contains 21 events
involving 7 claims and 13 registered sources. Each event encodes stable
claim and source identifiers, temporal ordering, evidence state,
uncertainty, lineage, and four separate status axes: epistemic,
diffusion, workflow, and documentary/record status. The public release
includes normalized CSV records, a codebook, source-boundary
documentation, a structural validator, mutation tests, and an integrity
manifest; complete private conversations and private source bytes are
not redistributed. The dataset is intended for qualitative and
structural studies of provenance, claim-state tracking, and
documentation practices in AI-assisted research. Its scale and
single-program design do not support population-level estimates of model
reliability, causal effects of human-AI collaboration, or large-scale
reward-model training.

# Background & Summary

Formal-mathematics datasets and benchmarks typically organize examples
around mathematical problems, theorem statements, formalizations, or
proof attempts. miniF2F provides 488 formal Olympiad-level problem
statements across several proof systems, while ProofNet pairs 371
undergraduate-level natural-language statements and proofs with Lean
theorem statements.<sup>6,7</sup>

A related line of work evaluates intermediate reasoning rather than only
final answers. In the MATH setting, process supervision outperformed
outcome supervision under the experimental conditions reported by
Lightman et al., who also released PRM800K with approximately 800,000
step-level human feedback labels.<sup>8</sup> These resources address
supervised reasoning at problem or step level; the present dataset
addresses a different unit of observation: the longitudinal change in
status of a scientific claim during an ongoing research process.

The representation of provenance and claim-level scientific information
has established precedents. W3C PROV provides a general model and
ontology for interoperable provenance; nanopublications separate an
assertion from its provenance and publication information;
micropublications model claims, evidence, arguments, and annotations;
and FAIR and RO-Crate practices emphasize reusable, machine-readable
research objects and their metadata.<sup>1,2,3,4,5</sup>

The dataset described here does not replace these general frameworks. It
records a small, source-linked sequence of claim-state transitions
observed within one AI-assisted mathematical research programme. The
frozen v1.1.2 snapshot contains 21 events, 13 registered sources, and 7
claims. Events include proposals, human vetoes, non-promotion after
statistical testing, restrictions of scope, exact finite verification,
refutation, documentary regression, provenance restoration, publication,
and transcription-error detection. The public corpus is deliberately
non-representative: it is intended to make specific trajectories
inspectable without implying population-level estimates of AI
reliability or causal effects of human-AI collaboration.

# Methods

## Unit of analysis and event inclusion

The unit of analysis is a claim-transition event rather than a complete
conversation, a file, or an AI model. A row records an observable
before/after change linked to a stable claim_id and source_id. Events
can affect one or more of four independent state axes. A transition may
therefore concern mathematical or empirical status, public visibility,
editorial/release workflow, documentary state, or a combination of these
dimensions.

Rows retain event dates, date granularity, within-day order where
available, actor type and role where supported, claim scope, control
type, control result, source-relative evidence state, uncertainty,
notes, and lineage. claim_parent_id and lineage_relation are used when a
restricted, split, or transcribed child claim must remain
distinguishable from its parent. The dataset does not claim exhaustive
reconstruction of every historical model interaction. Where a primary
source is unavailable or not redistributable, the available source type
and uncertainty are recorded rather than silently upgraded.

## Claim-boundary governance

Documentary and release rules were progressively introduced during the
programme to prevent finite computations, exploratory signals,
conditional statements, or publication decisions from being promoted
into broader mathematical claims. The release schema explicitly enforces
that publication or human veto alone cannot alter epistemic status. A
public release can therefore change diffusion and workflow while leaving
the mathematical status unchanged. The public snapshot documents this
governance framework; it does not establish that every historical
interaction was constrained by identical prompt-level guardrails.

## State model

The four status axes are encoded separately, with controlled
vocabularies defined in CODEBOOK.md. Evidence state is recorded as an
additional source-relative field rather than as a fifth claim-status
axis.

| **Axis**             | **Function**                               | **Examples from the controlled vocabulary**                                                                                                                           |
|----------------------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Epistemic            | Mathematical or empirical state of a claim | NA; PROPOSED; DEMOTED; REFUTED; VERIFIED_LOCAL; OBSERVED; NOT_PROMOTED; CANDIDATE_UNIFORM; SCOPE_RESTRICTED; VERIFIED_FINITE; PROVED_UNREVIEWED; FALSE_AS_STATED      |
| Diffusion            | Visibility of a claim or artefact          | NA; PRIVATE; PRIVATE_INTERNAL; PUBLIC                                                                                                                                 |
| Workflow             | Editorial or release process               | NA; PUBLICATION_PLANNED; BLOCKED; INTERNAL_RC; INTERNAL_CORRECTED; RELEASE_READY; RELEASED; HAL_READY                                                                 |
| Documentary / record | State of the documentary trace             | NA; RECORDED; REPORTED_MISSING; REDERIVED; RESTORED_ANTERIORITY; WITHDRAWN_BY_CHANGELOG; REASSERTED_UNCITED; MISTRANSCRIBED; DETECTED_UNCORRECTED; QUALIFIED_TENDENCY |

## Source registry and evidence state

Each source is assigned a source type, access class, date, locator or
non-redistribution identifier, analytical support statement, default
evidence state, and release eligibility. Evidence-state values include
PRIMARY_PUBLIC, PRIMARY_INTERNAL, PRIMARY_PRIVATE_COPY,
SECONDARY_PUBLIC, SECONDARY_INTERNAL, and RAW_PRESENT_REPLAYED. Primary
or secondary status is relative to the documented act; it is not a
global quality score. Event-level overrides require an explicit
justification in the event record.

## Snapshot freeze and later corrections

The released snapshot is not silently rewritten when later information
appears. Post-freeze developments are recorded outside the frozen counts
and can become new versioned events in a future dataset. This rule
preserves the historical trajectory rather than reconstructing a cleaner
sequence retrospectively. Documentary correction is also kept distinct
from mathematical correction: a source can be redated, restored, or
corrected without changing the epistemic state of the underlying claim.

## Privacy and source redaction

The public release does not redistribute complete private conversations,
private email messages, or private internal reports. For private or
internal sources, public locators can be replaced by
NOT_REDISTRIBUTED::\<source_id\>. Correspondent metadata and other
third-party identifiers are omitted where specified by the source
register. The released rows preserve the analytical relation between
events and sources while withholding the private source bytes. The
source register also records whether an item is public, private,
internal, replayed, or reconstructed so that users can distinguish
direct public evidence from restricted or retrospective evidence.

## Use of generative AI

Generative AI systems were used during the underlying research programme
for proposing, testing, drafting, and reviewing candidate mathematical
claims; actor_type and actor_role encode these roles where the sources
support them, and unresolved model identity remains unresolved.
Generative AI was also used as a drafting and editorial aid during
preparation of this Data Descriptor, including restructuring, language
revision, and literature retrieval. The author reviewed the source files
and cited literature and retains responsibility for the dataset,
manuscript content, and release decisions.

# Data Records

The frozen dataset v1.1.2 is distributed inside the archived public
reproducibility package version 1.1.0. The package and dataset use
separate version numbers: the package version identifies the archived
software/documentation release, whereas v1.1.2 identifies the frozen
event/source snapshot contained within it. The archive is cited as a
data/software record in reference 9.

| **File or object**              | **Contents**                                                                                                 | **Role**             |
|---------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------|
| data/events_v1.1.2.csv          | 21 normalized claim-transition events.                                                                       | Frozen dataset       |
| data/sources_v1.1.2.csv         | 13 registered sources with access classes, support statements, evidence defaults, and redistribution status. | Frozen dataset       |
| CODEBOOK.md                     | Field definitions, controlled vocabularies, evidence states, and structural invariants.                      | Public documentation |
| POSITIONING_AND_RELATED_WORK.md | Scope relative to provenance and claim-representation traditions.                                            | Public documentation |
| PUBLIC_SOURCE_BOUNDARY.md       | Public/private source boundary and redistribution rules.                                                     | Public documentation |
| POST_FREEZE_NOTES.md            | Later events and governance notes kept outside the frozen v1.1.2 counts.                                     | Public documentation |
| CONTROL_DESIGN.md               | Prospective control design for a future controlled study.                                                    | Public documentation |
| scripts/verify_release.py       | Deterministic structural validation suite.                                                                   | Public code          |
| MANIFEST_SHA256.txt             | Release integrity manifest.                                                                                  | Public manifest      |
| CITATION.cff and .zenodo.json   | Citation and archive metadata for the public package.                                                        | Public metadata      |

## Event record structure

events_v1.1.2.csv contains stable identifiers, claim lineage, time and
ordering fields, source and actor descriptors, a short claim label and
scope, control metadata, epistemic before/after states, evidence state,
diffusion before/after states, workflow before/after states,
documentary/record before/after states, transition_axis, human-guarantor
fields, transition reasons, uncertainty, and notes. The case_id field
groups rows into four historical trajectories labelled A-D without
treating those groups as statistically independent samples.

## External mathematical artefacts

Some event rows refer to mathematical artefacts that are not bundled
into the frozen dataset. These include the separate HOL-01 finite p=7
certificate, other finite-verification packages, manuscript records, and
private mathematical reports. Such artefacts retain their own versions,
licences, and validation procedures. Later HOL2 and Barning-Hall
materials post-date the frozen v1.1.2 snapshot and are therefore not
inserted retrospectively into the 21-event dataset.

# Technical Validation

## Structural validation

The public command python3 scripts/verify_release.py runs 517 structural
checks, four mutation tests, descriptive counts, frozen-byte and
metadata checks, and the release integrity manifest. The checks cover
unique identifiers, controlled vocabularies, source/access
compatibility, dates, within-day ordering, lineage, actual axis changes,
state chaining, claim-birth rules, evidence overrides, and the rule that
publication or veto alone cannot alter epistemic status. The expected
final line is RELEASE VERIFICATION: OK.

The mutation tests are designed to confirm that selected schema
violations are detected by the validator. They do not establish
completeness of the validator, and the 517 checks do not prove the
mathematical statements represented by the dataset. Mathematical
certificates, independent replay, literature review, and external peer
review remain separate forms of validation.

## Deterministic execution and integrity

The release validator requires Python 3.10 or later and uses only the
Python standard library. The package records frozen-file fingerprints
and a SHA-256 manifest. Historical CSV files and analytical scripts are
treated as immutable snapshot components; documentation on the current
branch can change only through versioned maintenance, while an archived
release remains fixed.

## Source-quality limitations

Not all event rows have the same source quality. Some are supported by
public primary artefacts, while others rely on private contemporary
copies, internal reports, replay logs, or retrospective reconstruction.
The source register and event-level uncertainty fields retain these
distinctions. In particular, the package cannot reconstruct unavailable
private source bytes, replay every historical experiment, establish
causal learning effects, or validate every mathematical assertion
represented in the event corpus.

# Usage Notes

The release can be used as a small reference corpus for parsers,
visualizations, provenance models, or claim-state classifiers that
operate on longitudinal research records. Users can reconstruct event
order, inspect which axes changed, compare source classes, or test
whether a system preserves distinctions between epistemic, documentary,
diffusion, and workflow states.

The dataset is not suitable for estimating general AI hallucination
rates, model reliability, or causal effects of long-term human-AI
interaction. Its 21 events are also not sufficient for large-scale
Process Reward Model training. Uses involving private source
reconstruction are outside the public release because the underlying
private conversations and reports are not redistributed. Future versions
can add new events, but corrections to the frozen v1.1.2 snapshot should
be versioned rather than silently substituted.

# Data Availability

The frozen v1.1.2 event/source dataset is distributed within Alexandre
Couret, “Qui répond des mathématiques produites par machine ? - public
reproducibility package”, version 1.1.0, Zenodo, DOI
[<u>10.5281/zenodo.23079572</u>](https://doi.org/10.5281/zenodo.23079572)
(reference 9). The corresponding public repository is
[<u>alexcour/qui-repond-mathematiques-ia</u>](https://github.com/alexcour/qui-repond-mathematiques-ia).
The associated manuscript is deposited in HAL as hal-05773424 (reference
10). Private source bytes referenced by NOT_REDISTRIBUTED::\<source_id\>
are not part of the public dataset.

# Code Availability

The structural validator, release-readiness checks, mutation tests, and
supporting scripts are distributed in the same public GitHub/Zenodo
package as the dataset. The primary reproducibility command is python3
scripts/verify_release.py under Python 3.10 or later; the validator uses
the Python standard library only. The public package is currently
released under the MIT License.

# References

**1.** Lebo, T. et al. PROV-O: The PROV Ontology. W3C Recommendation
(World Wide Web Consortium, 2013). https://www.w3.org/TR/prov-o/

**2.** Groth, P., Gibson, A. & Velterop, J. The anatomy of a
nanopublication. Information Services & Use 30, 51-56 (2010).
https://doi.org/10.3233/ISU-2010-0613

**3.** Clark, T., Ciccarese, P. N. & Goble, C. A. Micropublications: a
semantic model for claims, evidence, arguments and annotations in
biomedical communications. J. Biomed. Semant. 5, 28 (2014).
https://doi.org/10.1186/2041-1480-5-28

**4.** Wilkinson, M. D. et al. The FAIR Guiding Principles for
scientific data management and stewardship. Sci. Data 3, 160018 (2016).
https://doi.org/10.1038/sdata.2016.18

**5.** Soiland-Reyes, S. et al. Packaging research artefacts with
RO-Crate. Data Science 5, 97-138 (2022).
https://doi.org/10.3233/DS-210053

**6.** Zheng, K., Han, J. M. & Polu, S. MiniF2F: a cross-system
benchmark for formal Olympiad-level mathematics. Preprint at
https://arxiv.org/abs/2109.00110 (2021).

**7.** Azerbayev, Z., Piotrowski, B., Schoelkopf, H., Ayers, E. W.,
Radev, D. & Avigad, J. ProofNet: Autoformalizing and formally proving
undergraduate-level mathematics. Preprint at
https://arxiv.org/abs/2302.12433 (2023).

**8.** Lightman, H. et al. Let's Verify Step by Step. Preprint at
https://arxiv.org/abs/2305.20050 (2023).

**9.** Couret, A. Qui répond des mathématiques produites par machine ? -
public reproducibility package, version 1.1.0. Zenodo (2026).
https://doi.org/10.5281/zenodo.23079572

**10.** Couret, A. Qui répond des mathématiques produites par machine ?
Traçabilité longitudinale des transitions de revendications en recherche
mathématique assistée par IA. HAL hal-05773424 (2026).
https://hal.science/hal-05773424

# Author Contributions

A.C. conceived the claim-transition dataset, curated and normalized the
event and source records, defined the release governance and validation
requirements, reviewed the underlying research artefacts, and prepared
and revised the manuscript. A.C. is responsible for the final content
and release decisions.