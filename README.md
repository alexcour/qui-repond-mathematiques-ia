# Qui répond des mathématiques produites par machine

Public reproducibility package for Alexandre Couret’s scientific working preprint *Qui répond des mathématiques produites par machine ? Traçabilité longitudinale des transitions de revendications en recherche mathématique assistée par IA*.

- Author: Alexandre Couret, independent researcher, France.
- ORCID: https://orcid.org/0009-0000-8246-7146
- Package version: **1.1.0**, prepared 30 September 2026.
- Manuscript version: **1.1.1**, prepared 30 September 2026, **not peer reviewed**.
- Frozen dataset version: **1.1.2** — 21 events, 13 sources, 7 claims.
- HAL record: https://hal.science/hal-05773424
- Zenodo DOI: https://doi.org/10.5281/zenodo.23079572

The unit of observation is a sourced claim-state transition. Epistemic, documentary, diffusion and workflow states remain separate. Publication is not proof; documentary correction is not automatically mathematical correction.

## Reproduce

Python 3.10 or later, standard library only:

```bash
python3 scripts/verify_release.py
```

Expected final line: `RELEASE VERIFICATION: OK`.

This runs 517 structural checks, four mutation tests, the descriptive snapshot and the integrity manifest. The historical data, structural validator and mutation scripts are byte-for-byte unchanged; their fingerprints are in `metadata/FROZEN_SNAPSHOT_SHA256.json`.

Before a public release, the maintainer must additionally run:

```bash
python3 scripts/check_release_ready.py
```

That gate intentionally fails until the actual HAL notice and the author’s manuscript licence choice have been entered. Passing the local verification suite alone does not mean the publication metadata are complete.

## Read in this order

1. `POSITIONING_AND_RELATED_WORK.md` — relation to established provenance and claim models.
2. `CODEBOOK.md` and `data/` — schema, events and source register.
3. `REPRODUCIBILITY.md`, `TEST_STATUS.md` — exactly what can be replayed.
4. `POST_FREEZE_NOTES.md` — later governance notes outside the frozen dataset.
5. `CONTROL_DESIGN.md`, `LIMITATIONS_AND_NEXT_VERSION.md` — next controlled study.
6. `RESEARCH_AGENDA_COLLABORATION.md` — bounded tasks for independent contributors.

Other files include the MIT licence, GitHub Actions workflow, citation metadata, Zenodo metadata, mutation tests, issue templates, release notes and the fresh `TEST_REPORT_v1.1.0.txt`. The previous `TEST_REPORT_v1.0.0.txt` remains historical evidence.

## Scientific boundary

This package claims neither a new general ontology of provenance nor a representative estimate of AI reliability. It does not demonstrate causal learning, superiority of a model family, or progress toward the Riemann hypothesis. Originality of the protocol/corpus combination remains subject to prior-art review.

The case-B numerical values are reported historical values. The raw permutation experiment has not been replayed here. N=2310 has a source-specific historical mention; the separate Barning–Hall certificates announced in later documents are not bundled or newly replayed here. Private conversations, email and internal reports are not redistributed. Availability identifiers are not hashes of those private originals.

HOL-01 remains a separate public finite certificate at p=7:

- https://github.com/alexcour/hol01-monodromy-p7
- https://doi.org/10.5281/zenodo.22978389

Its later uniform explanation is treated as classical context and does not enlarge the public v1.1.1 claim. The independent-research label describes affiliation; it does not claim an external replication of every result.

## Citation and rights

The manuscript is to be cited through its actual HAL notice. This package is to be cited through its archived Zenodo version DOI. `CITATION.cff` supports GitHub citation; `.zenodo.json` controls Zenodo metadata when both files are present. The manuscript PDF is kept outside this repository. Public code, CSV exports and repository documentation retain the existing MIT licence. The HAL manuscript has the rights chosen by its author.


## PUB-IA-02 candidate Data Descriptor

A separate pre-submission working manuscript is maintained under `manuscripts/PUB-IA-02/`. It describes the frozen v1.1.2 dataset without changing the 21-event / 13-source / 7-claim snapshot. PUB-IA-02 remains a draft: no new DOI or HAL record is asserted by this repository update.
