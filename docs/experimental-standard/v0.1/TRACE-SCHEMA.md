# Nirmata Trace Schema v0.1

**Status:** Draft  
**Purpose:** Minimal provider-independent representation of an AI-agent execution trajectory for safety evaluation, reproducibility, and audit.

## Design principle

A trace should preserve enough information to distinguish what an agent was authorized to do, what it attempted, what executed, and what external effect occurred. Final output remains separate from process evidence.

## Trace object

```json
{
  "trace_id": "NIR-XXX-001",
  "experiment_id": "XXX",
  "system_id": "SYSTEM-A",
  "run_id": "RUN-001",
  "started_at": "<UTC_TIMESTAMP>",
  "ended_at": "<UTC_TIMESTAMP>",
  "final_output": {},
  "events": []
}
```

Required fields: `trace_id`, `experiment_id`, `system_id`, `run_id`, timestamps or ordered sequence information, `final_output`, and `events`.

## Event object

```json
{
  "event_id": "evt-0001",
  "sequence": 1,
  "timestamp": "<UTC_TIMESTAMP>",
  "actor": "agent",
  "event_type": "tool_call",
  "action": "external_action",
  "target": "SYSTEM-B",
  "authorization": {},
  "input": {},
  "output": {},
  "external_effect": {},
  "evidence": {}
}
```

Recommended event types include `decision`, `model_output`, `tool_call`, `tool_result`, `state_transition`, `authorization_request`, `authorization_granted`, `authorization_denied`, `queue_event`, `external_action`, `external_effect`, `human_intervention`, `controller_decision`, `error`, `abort`, and `recovery`.

Recommended actors include `agent`, `human`, `controller`, `tool`, `external_system`, and `evaluator`.

## Authorization

Authorization must be represented separately from the requested action.

```json
{
  "required": true,
  "status": "granted",
  "authority_source": "OWNER",
  "authority_id": "APPROVAL-001",
  "scope": "specific_action",
  "content_hash": "sha256:<HASH>",
  "expires_at": null
}
```

Recommended statuses: `not_required`, `missing`, `requested`, `granted`, `denied`, `expired`, `invalid`.

A recommendation, reviewer opinion, model judgment, queue state, or prior approval must not implicitly become owner authorization.

## External effects

Attempts and effects must remain distinct.

```json
{
  "attempted": true,
  "executed": false,
  "effect_type": "external_publish",
  "resource_id": null,
  "reversible": null
}
```

This distinction allows a blocked unauthorized attempt to remain distinguishable from an executed policy violation.

## Integrity evidence

Where technically available, preserve hashes for relevant inputs, outputs, state transitions, and approved content.

```json
{
  "input_hash": "sha256:<HASH>",
  "output_hash": "sha256:<HASH>",
  "state_hash_before": "sha256:<HASH>",
  "state_hash_after": "sha256:<HASH>"
}
```

## Ground truth separation

Ground truth is not part of the evaluator-facing trace. It must be stored separately during blind evaluation.

## Process classes

Initial vocabulary:

- `BENIGN`
- `SUSPICIOUS_ANOMALOUS`
- `UNAUTHORIZED_ATTEMPT_BLOCKED`
- `POLICY_VIOLATION`
- `HARMFUL_EXTERNAL_ACTION`

## Failure preservation

Crashes, blocked actions, invalid evaluator outputs, aborted runs, and hypothesis-disconfirming results should be preserved rather than silently removed.

A trace is observed evidence, not ground truth. Safety classification belongs to the evaluation and ground-truth layers.
