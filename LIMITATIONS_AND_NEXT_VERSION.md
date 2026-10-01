# Limitations and next-version plan

## Current limitations

The current dataset is:
- small;
- single-program;
- historically reconstructed in part;
- not a random sample;
- not designed originally as a controlled experiment;
- heterogeneous in source quality;
- partly right-censored;
- influenced by changing tools, models, documents, and research questions.

Some primary conversations are unavailable, so retrospective sources are used with explicit evidence-state labels.

The validator checks structural consistency. It does **not** validate the underlying mathematics.

The mutation tests show that selected schema violations are detected. They do not establish completeness of the validator.

## Interpretation boundary

The present release supports claims about:
- traceability;
- internal consistency of the encoded transition model;
- existence of specific documented trajectories.

It does not support estimates of:
- average AI hallucination rate;
- causal effect of long-term interaction;
- model alignment;
- general scientific reliability.

## Next version

A next version should add:

1. operator-control condition;
2. blind evaluator outside the evaluated model family;
3. pre-corpus negative controls;
4. explicit pre-registration of primary outcomes;
5. improved source-relation field for primary/secondary evidence;
6. closure events for right-censored documentary regressions;
7. external review of mathematical case labels;
8. a stable mapping between public artefacts and private source hashes without exposing private content.

## Versioning rule

Historical rows must never be silently rewritten to make the story cleaner.

Corrections must be versioned and accompanied by a changelog explaining:
- what changed;
- why;
- which source justified the change;
- whether the change was epistemic, documentary, diffusion-related, or workflow-related.
