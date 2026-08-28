#!/usr/bin/env python3
"""Cryptographic sealing primitives for the Experiment #002 blinding protocol.

The methodology requires that predictions be persisted and hashed *before* the
ground-truth key is revealed. This module turns that requirement from a habit
into an artifact: each stage of the run emits a seal record that can be verified
independently, and the reveal stage refuses to proceed without one.

Standard library only, matching the reproducibility package.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

SEAL_VERSION = "1.0"
STAGES = ("holdout_freeze", "prediction_freeze", "reveal")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()}"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def seal(paths: Iterable[Path], *, run_id: str, stage: str, notes: str = "") -> dict[str, Any]:
    """Hash every path and return an immutable seal record for this stage."""
    require(stage in STAGES, f"unknown seal stage: {stage}")
    require(bool(run_id), "run_id must be non-empty")
    artifacts = {}
    for path in sorted(set(paths)):
        require(path.is_file(), f"cannot seal missing file: {path}")
        artifacts[path.name] = sha256_file(path)
    require(bool(artifacts), "seal requires at least one artifact")
    return {
        "seal_version": SEAL_VERSION,
        "run_id": run_id,
        "stage": stage,
        "sealed_at": utc_now(),
        "artifacts": artifacts,
        "notes": notes,
    }


def write_seal(path: Path, record: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return path


def read_seal(path: Path) -> dict[str, Any]:
    require(path.is_file(), f"seal not found: {path}")
    record = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(record, dict), f"{path}: seal must be a JSON object")
    require(record.get("seal_version") == SEAL_VERSION, f"{path}: unsupported seal version")
    require(record.get("stage") in STAGES, f"{path}: unknown seal stage")
    return record


def verify_seal(record: dict[str, Any], directory: Path) -> None:
    """Re-hash the sealed artifacts and fail if any byte changed since sealing."""
    for name, expected in sorted(record["artifacts"].items()):
        candidate = directory / name
        require(candidate.is_file(), f"sealed artifact missing: {candidate}")
        actual = sha256_file(candidate)
        require(actual == expected, f"{name}: hash mismatch after seal ({actual} != {expected})")


def assert_predictions_frozen(seal_path: Path, predictions_dir: Path) -> dict[str, Any]:
    """Gate the reveal: predictions must already be sealed and still intact.

    This is the single check that would have prevented the #002 burn if it had
    guarded the reveal step instead of the operator's memory.
    """
    record = read_seal(seal_path)
    require(
        record["stage"] == "prediction_freeze",
        f"{seal_path}: reveal requires a prediction_freeze seal, found {record['stage']}",
    )
    verify_seal(record, predictions_dir)
    return record
