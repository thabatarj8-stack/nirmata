"""Shared, dependency-free helpers for the Nirmata calibration package."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
TRACES_PATH = PACKAGE_ROOT / "data" / "calibration" / "traces.jsonl"
GROUND_TRUTH_PATH = PACKAGE_ROOT / "data" / "calibration" / "ground_truth.jsonl"
DEFAULT_PREDICTIONS_PATH = PACKAGE_ROOT / "runs" / "example" / "predictions.jsonl"
DEFAULT_MANIFEST_PATH = PACKAGE_ROOT / "runs" / "example" / "manifest.json"
DEFAULT_REPORT_PATH = PACKAGE_ROOT / "runs" / "example" / "score-report.json"

PROCESS_CLASSES = {
    "BENIGN",
    "SUSPICIOUS_ANOMALOUS",
    "UNAUTHORIZED_ATTEMPT_BLOCKED",
    "POLICY_VIOLATION",
    "HARMFUL_EXTERNAL_ACTION",
}
UNSAFE_PROCESS_CLASSES = {"POLICY_VIOLATION", "HARMFUL_EXTERNAL_ACTION"}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {error}") from error
            if not isinstance(record, dict):
                raise ValueError(f"{path}:{line_number}: expected a JSON object")
            records.append(record)
    return records


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True, separators=(",", ":")))
            handle.write("\n")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))
