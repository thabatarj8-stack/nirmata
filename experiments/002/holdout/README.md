# Experiment #002 Holdout

**Status:** Pre-freeze design area

This directory defines handling rules for a fresh blind confirmatory holdout. It must not contain the previously exposed answer key as confirmatory evidence.

## Target size

Initial confirmatory pilot target: **12 matched traces**.

The exact final composition must be frozen before execution.

## Intended class distribution

- `BENIGN`: 3
- `SUSPICIOUS_ANOMALOUS`: 2
- `UNAUTHORIZED_ATTEMPT_BLOCKED`: 2
- `POLICY_VIOLATION`: 3
- `HARMFUL_EXTERNAL_ACTION`: 2

## Intended evidence mix

The holdout should include a mixture of:

- safe final output + safe trajectory;
- safe-looking final output + unsafe trajectory;
- unsafe final output;
- blocked unauthorized attempts.

Failure families should span at least:

- authority;
- content integrity;
- state/control;
- external effect.

## Inclusion criteria

A case may enter the confirmatory holdout only if:

- the trajectory is complete enough to evaluate;
- the final output is available;
- events are temporally ordered or have a stable sequence;
- authorization state is observable when relevant;
- external-effect status is known when relevant;
- ground truth can be justified independently;
- sanitization preserves safety-relevant semantics.

## Exclusion criteria before freeze

Exclude cases with missing required evidence, materially ambiguous ground truth, accidental answer labels, privacy sanitization that destroys the relevant semantics, or material duplication.

After freeze, cases must not be removed merely because they reduce measured performance.

## Ground truth

Ground truth must be stored separately from evaluator-facing traces and must not be exposed to evaluators before prediction freeze.

A private rationale may be maintained for audit, but it must not appear in evaluator inputs.

## Synthetic identifiers

Use IDs such as:

```text
NIR-002-H2-001
NIR-002-H2-002
...
```

Do not encode real names, usernames, customer identities, account identifiers, or other unnecessary identifying information in trace IDs or metadata.

## Sanitization

The evaluator-facing dataset should be sanitized before its final freeze and hash. Sanitization must remove unnecessary sensitive data while preserving the relationships needed to evaluate authorization, state transitions, tool use, and external effects.

## Freeze requirements

Before the holdout is marked `FROZEN`:

- all expected traces exist;
- synthetic IDs are assigned;
- privacy review is complete;
- class balance is fixed;
- inclusion criteria are checked;
- ground truth is finalized and separately held;
- evaluator-facing traces are frozen and hashed;
- the sealed ground-truth artifact is hashed;
- neither evaluator has seen the ground truth.

## Burned holdouts

Any holdout whose answer key becomes available to an evaluator before prediction freeze is burned for blind confirmatory use with that evaluator context. It may still be retained for development, debugging, demonstration, or regression testing.
