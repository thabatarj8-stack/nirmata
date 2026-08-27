#!/usr/bin/env python3
"""Validate structural and integrity invariants for public calibration data."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

from common import (
    APPLIED_DATA_PATH,
    GROUND_TRUTH_PATH,
    PROCESS_CLASSES,
    TRACES_PATH,
    UNSAFE_PROCESS_CLASSES,
    load_jsonl,
    sha256_text,
)


REQUIRED_TRACE_KEYS = {"schema_version", "trajectory_id", "task", "final_output", "events"}
REQUIRED_EVENT_KEYS = {"sequence", "type", "actor", "outcome"}
EVENT_TYPES = {"decision", "tool_call", "authorization", "state_transition", "external_effect", "human_intervention"}
OUTCOMES = {"allowed", "blocked", "executed", "failed", "observed"}
ALLOWED_EVENT_KEYS = REQUIRED_EVENT_KEYS | {"action", "authorization", "external_effect", "evidence"}
TRAJECTORY_ID = re.compile(r"^[a-z0-9][a-z0-9._-]+$")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_trace(trace: dict[str, Any]) -> None:
    trace_id = trace.get("trajectory_id", "<missing>")
    require(set(trace) == REQUIRED_TRACE_KEYS, f"{trace_id}: unexpected or missing top-level keys")
    require(trace["schema_version"] == "0.1.0", f"{trace_id}: unsupported schema version")
    require(isinstance(trace_id, str) and TRAJECTORY_ID.fullmatch(trace_id) is not None, f"{trace_id}: invalid trajectory_id")
    require(isinstance(trace["task"], str) and trace["task"], f"{trace_id}: task must be non-empty")

    final_output = trace["final_output"]
    require(isinstance(final_output, dict), f"{trace_id}: final_output must be an object")
    require(set(final_output) == {"content", "content_hash"}, f"{trace_id}: invalid final_output keys")
    require(isinstance(final_output["content"], str), f"{trace_id}: final output content must be a string")
    expected_hash = f"sha256:{sha256_text(final_output['content'])}"
    require(final_output["content_hash"] == expected_hash, f"{trace_id}: final output hash mismatch")

    events = trace["events"]
    require(isinstance(events, list) and events, f"{trace_id}: events must be non-empty")
    require([event.get("sequence") for event in events] == list(range(1, len(events) + 1)), f"{trace_id}: event sequence must be contiguous")
    for event in events:
        require(REQUIRED_EVENT_KEYS <= set(event), f"{trace_id}: event missing required keys")
        require(set(event) <= ALLOWED_EVENT_KEYS, f"{trace_id}: event has unexpected keys")
        require(isinstance(event["sequence"], int) and event["sequence"] > 0, f"{trace_id}: invalid event sequence")
        require(event["type"] in EVENT_TYPES, f"{trace_id}: unknown event type")
        require(isinstance(event["actor"], str) and event["actor"], f"{trace_id}: invalid event actor")
        require(event["outcome"] in OUTCOMES, f"{trace_id}: unknown event outcome")
        if "action" in event:
            require(isinstance(event["action"], str), f"{trace_id}: event action must be a string")
        if "authorization" in event:
            authorization = event["authorization"]
            require(isinstance(authorization, dict), f"{trace_id}: authorization must be an object")
            require(set(authorization) == {"principal", "scope", "decision"}, f"{trace_id}: invalid authorization keys")
            require(authorization["decision"] in {"granted", "denied", "missing", "invalid"}, f"{trace_id}: invalid authorization decision")
        if "external_effect" in event:
            effect = event["external_effect"]
            require(isinstance(effect, dict), f"{trace_id}: external_effect must be an object")
            require("occurred" in effect and set(effect) <= {"occurred", "system", "effect_id"}, f"{trace_id}: invalid external_effect keys")
            require(isinstance(effect["occurred"], bool), f"{trace_id}: occurred must be boolean")
        if "evidence" in event:
            require(isinstance(event["evidence"], dict), f"{trace_id}: evidence must be an object")


def validate_package(traces_path: Path = TRACES_PATH, truth_path: Path = GROUND_TRUTH_PATH) -> dict[str, int]:
    traces = load_jsonl(traces_path)
    truth = load_jsonl(truth_path)
    for trace in traces:
        validate_trace(trace)

    trace_ids = [record["trajectory_id"] for record in traces]
    truth_ids = [record.get("trajectory_id") for record in truth]
    require(len(trace_ids) == len(set(trace_ids)), "duplicate trajectory IDs")
    require(len(truth_ids) == len(set(truth_ids)), "duplicate ground-truth IDs")
    require(set(trace_ids) == set(truth_ids), "trace and ground-truth IDs differ")

    for record in truth:
        trace_id = record["trajectory_id"]
        require(set(record) == {"trajectory_id", "content_unsafe", "trajectory_class", "trajectory_unsafe"}, f"{trace_id}: invalid ground-truth keys")
        process_class = record.get("trajectory_class")
        require(process_class in PROCESS_CLASSES, f"{trace_id}: invalid process class")
        require(isinstance(record.get("content_unsafe"), bool), f"{trace_id}: content_unsafe must be boolean")
        require(isinstance(record.get("trajectory_unsafe"), bool), f"{trace_id}: trajectory_unsafe must be boolean")
        require(record["trajectory_unsafe"] == (process_class in UNSAFE_PROCESS_CLASSES), f"{trace_id}: unsafe flag conflicts with process class")

    applied = 0
    if APPLIED_DATA_PATH.exists():
        for path in sorted(APPLIED_DATA_PATH.glob("*.json")):
            record = json.loads(path.read_text(encoding="utf-8"))
            require(isinstance(record, dict), f"{path}: applied trace must be an object")
            validate_trace(record)
            applied += 1

    return {"traces": len(traces), "labels": len(truth), "applied": applied}


def main() -> int:
    try:
        json.loads((Path(__file__).resolve().parents[1] / "schema" / "trajectory.schema.json").read_text(encoding="utf-8"))
        result = validate_package()
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"validation failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps({"status": "ok", **result}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
