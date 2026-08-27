# Experiment registry

This registry distinguishes exploratory observations, development checks, integration validation, and confirmatory evidence.

## Experiment 001

### Strategic agent evaluation and delegated authority

An editorial agent selected and verified a topic, but its trajectory incorrectly converted a reviewer's recommendation into owner approval. The final draft was acceptable; the authorization path was not. This observation motivated trajectory-aware evaluation.

Follow-up development and control-integrity suites tested approval injection, forged identity, state tampering, content substitution, queue tampering, replay, and two-phase publication. Twelve known checks passed. Because the checks were visible during implementation and the control plane was not isolated at OS level, they support implementation behavior on known cases rather than generalization or production security.

## Experiment 002

### Final-output evaluation versus independent trajectory signal

The current design uses a shared content judgment and an independent trajectory judgment, combined with a deterministic OR. Integration validation passed on six calibration cases after earlier evaluator designs and their failures were preserved.

A separate [public synthetic fixture](../reproducibility/README.md) now makes the factorized plumbing executable with transparent cases and deterministic expected outputs. It demonstrates package integrity only and is not the original Run 002.0d dataset or evidence of evaluator generalization.

The planned blind confirmatory run did not occur. The ground-truth file was accidentally exposed to the evaluator context before predictions were produced. No predictions or metrics were generated, and the holdout was invalidated for that context. A fresh holdout is required.

## Experiment 003

### Evaluator context interference — candidate study

During integration work, a joint-context evaluator sometimes allowed clean trajectory evidence to interfere with detection of independently unsafe content. This is a motivating observation for a separate experiment, not a confirmed general effect. The study has not started.

## Evidence labels used by this repository

- `EXPLORATORY`: observation that motivates a question.
- `DEVELOPMENT`: known tests used to implement or debug a system.
- `INTEGRATION`: pipeline or component validation on calibration cases.
- `CONFIRMATORY`: blind evaluation on frozen, unseen data.
- `INVALIDATED`: evidence that cannot support the intended claim because a protocol condition failed.
