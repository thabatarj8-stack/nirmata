# Nirmata Run Manifest v0.1

**Status:** Draft  
**Purpose:** Define a machine-readable provenance record for experimental runs.

A run manifest answers: under exactly what recorded conditions was this result produced?

## Minimum structure

```json
{
  "schema": "nirmata-run-manifest",
  "schema_version": "0.1",
  "run_id": "RUN-001",
  "experiment_id": "XXX",
  "protocol_version": "1.0",
  "run_type": "confirmatory",
  "status": "planned",
  "protocol": {},
  "dataset": {},
  "evaluators": {},
  "aggregation": {},
  "predictions": {},
  "ground_truth_custody": {},
  "authorization_context": {},
  "environment": {},
  "protocol_deviations": [],
  "scoring": {},
  "evidence": {
    "intended_class": "CONFIRMATORY",
    "final_class": null,
    "valid": null
  }
}
```

Recommended run types: `exploratory`, `development`, `integration`, `confirmatory`.

Recommended statuses: `planned`, `running`, `completed`, `aborted`, `invalidated`.

## Protocol provenance

Record the protocol version, file reference, and SHA-256 where available. Protocol changes must create an explicit new version rather than silently replacing the frozen record.

## Dataset provenance

Record dataset ID, version, trace count, evaluator-facing trace artifact hash, and the separately held ground-truth artifact hash where appropriate. The public manifest need not expose a sealed ground-truth artifact.

## Evaluators

Record evaluator identifiers, provider/model identifiers, configuration, prompt versions, and prompt hashes where technically available. If exact model weights or versions are provider-managed, record that limitation rather than implying stronger reproducibility.

## Predictions and reveal

Record when predictions were persisted and hashed and whether this occurred before ground-truth reveal.

## Deviations

Protocol deviations should be recorded with a stable ID, description, timestamp when available, and severity: `non_material`, `material`, or `invalidating`.

## Aborts

Aborted runs remain part of the research record. Record the stage, reason, whether predictions existed, and whether metrics were generated.

## Environment

Record repository commit, runtime information, dependency lockfile/hash, and other environment metadata available for reproduction. Unknown or unavailable information should be stated explicitly.

## Evidence Downgrade Principle

Evidence classification may be downgraded after execution but never upgraded beyond the class permitted by the frozen protocol. A development run cannot become confirmatory merely because its result is favorable.
