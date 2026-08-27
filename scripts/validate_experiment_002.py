#!/usr/bin/env python3
"""Validate Experiment 002 schemas and the public template artifacts."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "experiments" / "002"
SCHEMAS = EXPERIMENT / "schemas"


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validator(name: str) -> Draft202012Validator:
    schema = load_json(SCHEMAS / name)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_jsonl(path: Path, artifact_validator: Draft202012Validator) -> int:
    count = 0
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            artifact = json.loads(line)
            errors = sorted(artifact_validator.iter_errors(artifact), key=lambda error: list(error.path))
            if errors:
                locations = ", ".join(
                    f"line {line_number} /{'/'.join(map(str, error.path)) or '<root>'}: {error.message}"
                    for error in errors
                )
                raise ValueError(f"{path.relative_to(ROOT)}: {locations}")
            count += 1
    if count == 0:
        raise ValueError(f"{path.relative_to(ROOT)} contains no predictions")
    return count


def main() -> None:
    trace_validator = validator("trace.schema.json")
    prediction_validator = validator("prediction.schema.json")
    manifest_validator = validator("run-manifest.schema.json")

    minimal_trace = {
        "trace_id": "NIR-002-SCHEMA-CHECK",
        "experiment_id": "002",
        "system_id": "schema-check",
        "run_id": "NIR-002-SCHEMA-CHECK",
        "final_output": {"type": "text", "content": "synthetic validation fixture"},
        "events": [
            {
                "event_id": "event-001",
                "sequence": 0,
                "actor": "agent",
                "event_type": "model_output",
            }
        ],
    }
    trace_validator.validate(minimal_trace)

    manifest = load_json(EXPERIMENT / "manifests" / "run-manifest.template.json")
    manifest_validator.validate(manifest)

    content_count = validate_jsonl(
        EXPERIMENT / "predictions" / "content-predictions.template.jsonl",
        prediction_validator,
    )
    trajectory_count = validate_jsonl(
        EXPERIMENT / "predictions" / "trajectory-predictions.template.jsonl",
        prediction_validator,
    )
    expected_count = manifest["dataset"]["trace_count"]
    if content_count != expected_count or trajectory_count != expected_count:
        raise ValueError(
            "prediction template counts must match dataset.trace_count "
            f"({expected_count}); received content={content_count}, trajectory={trajectory_count}"
        )

    load_json(EXPERIMENT / "manifests" / "freeze-record.template.json")
    print(
        "Experiment 002 artifacts: ok "
        f"({content_count} content predictions, {trajectory_count} trajectory predictions)"
    )


if __name__ == "__main__":
    main()
