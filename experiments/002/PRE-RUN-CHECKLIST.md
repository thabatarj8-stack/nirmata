# Experiment #002 Pre-Run Checklist v1.0

**Status:** Pre-freeze

This checklist must be completed before a confirmatory run begins. It does not contain ground truth.

## Protocol

- [ ] Protocol v1.0 finalized
- [ ] Primary and secondary hypotheses frozen
- [ ] Aggregation rule frozen
- [ ] Inclusion/exclusion rules frozen
- [ ] Invalidation rules frozen
- [ ] Protocol SHA-256 recorded

## Holdout

- [ ] Fresh holdout created
- [ ] Exactly 12 evaluator-facing traces selected
- [ ] Synthetic case IDs assigned
- [ ] Class/failure-family composition fixed
- [ ] No answer labels embedded in traces
- [ ] Sanitization completed
- [ ] Safety-relevant semantics preserved after sanitization
- [ ] `traces.jsonl` frozen and hashed

## Ground truth custody

- [ ] Ground truth finalized separately
- [ ] Ground truth inaccessible to evaluators
- [ ] Ground-truth hash recorded privately or as sealed metadata
- [ ] No ground-truth information exists in evaluator prompts or trace metadata

## Evaluators

- [ ] Content evaluator prompt finalized and hashed
- [ ] Trajectory evaluator prompt finalized and hashed
- [ ] Provider/model/configuration recorded
- [ ] Output schemas frozen
- [ ] Content evaluator cannot access trajectory classification
- [ ] Trajectory evaluator cannot access content-evaluator classification
- [ ] Neither evaluator can access ground truth

## Scoring

- [ ] Scoring Specification v0.1 frozen
- [ ] Primary metrics frozen
- [ ] Missing/invalid prediction handling frozen
- [ ] No-abstention rule confirmed unless protocol says otherwise
- [ ] Scoring implementation/hash recorded when available

## Publication safety

- [ ] Personal names removed where scientifically unnecessary
- [ ] Usernames/handles removed
- [ ] Client/customer identities removed
- [ ] Private organization identifiers generalized where needed
- [ ] Emails and phone numbers removed
- [ ] Credentials, tokens, secrets, session IDs, and private URLs absent
- [ ] Internal paths and unnecessary infrastructure details removed
- [ ] Public artifacts use synthetic identifiers

## Manifest and contamination check

- [ ] Run manifest populated with known pre-run metadata
- [ ] Intended evidence class is `CONFIRMATORY`
- [ ] Evaluators have not seen the holdout answer key
- [ ] Evaluators have not seen these exact holdout cases paired with labels
- [ ] Evaluator inputs contain no answer-revealing metadata

If any contamination check fails, stop. Do not run the affected holdout as blind confirmatory evidence.

## Freeze record

Before execution:

- [ ] Freeze record populated
- [ ] Required hashes recorded
- [ ] Freeze timestamp recorded in UTC
- [ ] `ground_truth_withheld` is true
- [ ] `privacy_review_completed` is true
- [ ] Status changed to `FROZEN`

## After evaluator execution, before reveal

- [ ] All expected content predictions generated or failures recorded
- [ ] All expected trajectory predictions generated or failures recorded
- [ ] Prediction schemas validated
- [ ] No manual corrections performed
- [ ] Prediction artifacts persisted
- [ ] Prediction hashes recorded
- [ ] Protocol deviations recorded
- [ ] Ground truth remains unrevealed

Only after this section is complete may ground-truth reveal and frozen scoring occur.

## Final evidence decision

A valid run may end as:

- `CONFIRMATORY` with hypothesis supported
- `CONFIRMATORY` with hypothesis not supported
- `CONFIRMATORY` with inconclusive pilot evidence
- `INVALIDATED`

A negative result is not an invalid run. Protocol validity and hypothesis outcome are separate questions.
