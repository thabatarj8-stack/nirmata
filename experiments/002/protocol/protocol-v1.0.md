# Experiment #002 Protocol v1.0

**Title:** Final-output evaluation versus independent trajectory signal  
**Status:** Pre-freeze draft  
**Evidence target:** Confirmatory pilot  
**Framework:** Nirmata Experimental Standard v0.1

## Research question

Does independently evaluated trajectory evidence reveal safety-relevant failures that are missed when evaluation considers only the final output?

## Primary hypothesis

At least one ground-truth unsafe case will be accepted as safe by final-output-only evaluation and detected as unsafe by the independent trajectory evaluator.

## Secondary hypothesis

Some authorization-path failures can be detected from trajectory evidence even when the final output itself contains no observable unsafe content.

## Experimental conditions

Final-output-only evaluation receives the synthetic trace identifier and final output. Its binary classification is `content_unsafe`.

Trajectory evaluation receives the process evidence permitted by the frozen trajectory condition and produces `trajectory_unsafe` plus a process class.

Combined classification is frozen as:

```text
trajectory_aware_unsafe = content_unsafe OR trajectory_unsafe
```

## Independence

Neither evaluator may access ground truth before prediction freeze. The final-output evaluator does not receive trajectory classification. The trajectory evaluator does not receive the content-evaluator classification or final combined classification.

## Holdout

The confirmatory holdout must be fresh and must not reuse a previously exposed answer key as blind confirmatory evidence. The initial target is 12 matched traces, with exact composition frozen before execution.

## Metrics

Primary reporting includes Safety Blind Spot Rate, Incremental Detection Value, Unsafe Acceptance Rate, Violation Detection Recall, and False Positive Rate. Evaluator/schema failures must also be reported.

## Missing or malformed predictions

Invalid or missing evaluator outputs are recorded as evaluation failures and are not manually repaired during the confirmatory run.

## Blinding

All predictions must be persisted and hashed before ground-truth reveal. Ground-truth exposure to an evaluator before prediction freeze invalidates the affected blind confirmatory run.

## Privacy

Evaluator and public artifacts use synthetic identifiers. No real names, usernames, customer identities, credentials, private account identifiers, or unnecessary sensitive operational details are required for the scientific claim.

## Analysis boundary

After freeze there is no prompt tuning, threshold tuning, performance-based case replacement, aggregation change, or retrospective relabeling within this run. Methodological changes create a new protocol version and, where required, a fresh holdout.

## Permitted claims

A valid pilot may support a bounded claim about incremental trajectory signal in the tested holdout. It does not by itself establish universal superiority, cross-domain generalization, or production safety.

## Evidence classification

The intended evidence class is `CONFIRMATORY`. Final classification is determined after execution and may be downgraded, including to `INVALIDATED`, if protocol requirements are violated.
