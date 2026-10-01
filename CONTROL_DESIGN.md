# Control design for the next study version

This file defines controls required before the pilot protocol can support stronger empirical conclusions.

## 1. Operator control

The same prompt or task package should be submitted by a second human operator who was not involved in the original research episode.

Purpose:
- separate properties of the model/system from Alexandre Couret's accumulated interaction history;
- reduce confounding by prompt phrasing habits, context management, or operator-specific follow-up behavior.

The operator control must preserve:
- prompt text;
- supplied files;
- tool permissions;
- model/version when technically possible;
- stopping rules.

Differences must be logged, not silently normalized.

## 2. Blind evaluator

Evaluation should be performed by a reviewer who:
- is not part of the model family being evaluated;
- does not know which condition produced each transcript when blinding is feasible;
- applies a predeclared rubric.

At least part of the evaluation should be human.

## 3. Pre-corpus negative controls

Events predating the focal corpus must be used where available.

In particular, an earlier machine-side refusal or disciplined non-promotion before exposure to the later corpus is relevant evidence against a simple “the corpus taught the system restraint” explanation.

Such controls do not prove absence of learning; they constrain causal interpretation.

## 4. Factorial design

A future controlled phase should separate at least:

A. operator;
B. model or model family;
C. access to prior corpus/context;
D. task type.

A minimal design should avoid changing all factors simultaneously.

## 5. Outcomes

Primary outcomes should be defined before running the study.

Examples:
- unsupported promotion rate;
- scope-restriction rate;
- rate of correct distinction between finite evidence and theorem;
- detection of prior-art conflicts;
- documentary/provenance correction rate;
- time or turns to stable claim boundary.

## 6. Blindness and adjudication

Disagreements should be adjudicated by a procedure fixed in advance.

If an external expert is required for the mathematics, that expertise should be separated from the model-performance evaluation where possible.

## 7. Claim boundary

The pilot v1.0 remains a longitudinal case study.

It does not establish:
- causal learning by the model;
- population-level AI reliability;
- superiority of one model family;
- a universal theory of scientific responsibility.
