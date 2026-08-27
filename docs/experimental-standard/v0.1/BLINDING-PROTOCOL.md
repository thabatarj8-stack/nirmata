# Nirmata Blinding Protocol v0.1

**Status:** Draft

## Core rule

No component producing a confirmatory prediction may access the answer key before its predictions are frozen.

## Logical roles

A blind run separates four information roles: case author, ground-truth custodian, evaluator, and scorer. These need not be four people, but the information boundaries must be preserved.

## Freeze

Before a confirmatory holdout run, freeze the hypothesis, dataset definition, evaluator prompts, model configuration, schemas, aggregation rule, scoring rules, exclusion criteria, and invalidation criteria. Record hashes where technically possible.

Changes made after observing holdout behavior require a new version and must not be represented as part of the original confirmatory protocol.

## Evaluator isolation

A final-output evaluator receives only the evidence permitted by the final-output condition. A trajectory evaluator receives only the process evidence permitted by the trajectory condition. Neither receives ground truth before prediction freeze.

Ground truth should be technically inaccessible where feasible, not merely hidden by instruction.

## Context contamination

If ground truth enters an evaluator context before predictions are persisted, the affected holdout is invalid for blind confirmatory use with that evaluator context. Deletion, instruction, or claimed non-use does not restore blindness.

### Epistemic Irreversibility Principle

Once information forbidden by a blind protocol crosses the evaluation boundary, that blindness cannot be restored by instruction, deletion, or intention.

## Prediction freeze

Before ground-truth reveal:

1. all expected predictions are generated or missing outputs are recorded according to the frozen protocol;
2. predictions are persisted;
3. the prediction artifact is hashed;
4. deviations are recorded;
5. evaluator execution is complete.

Only then may the reveal barrier be crossed.

## Invalidating events

Examples include ground-truth exposure, answer labels embedded in evaluator inputs, prediction modification after reveal, post-hoc evaluator-prompt changes based on holdout behavior, post-hoc aggregation changes, post-hoc scoring changes, and replacement of holdout cases based on performance.

## Burned holdouts

A holdout exposed to its answer key may still be used for development, debugging, demonstration, or regression testing, but not as blind confirmatory evidence for the affected context.

## Operational failures

Technical failures such as network interruption or service outage are not automatically scientific invalidation. They must remain visible and be handled according to rules frozen before reveal.

## Post-reveal rule

Confirmatory predictions are not manually repaired after ground-truth reveal. Error analysis may motivate a new evaluator version, but that version requires fresh confirmatory evidence.

## Evidence downgrade

Evidence classification may be downgraded after execution but never upgraded beyond the class permitted by the frozen protocol.
