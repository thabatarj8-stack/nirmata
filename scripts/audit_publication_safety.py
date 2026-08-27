#!/usr/bin/env python3
"""Fail on high-confidence secrets or direct identifiers in public artifacts."""

from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAX_TEXT_SIZE = 2 * 1024 * 1024


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]


RULES = (
    Rule("private key", re.compile(r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----")),
    Rule("AWS access key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    Rule("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    Rule("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    Rule("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    Rule("OpenAI API key", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b")),
    Rule("Stripe live key", re.compile(r"\b[sr]k_live_[A-Za-z0-9]{16,}\b")),
    Rule(
        "credential-bearing URL",
        re.compile(r"\b[a-z][a-z0-9+.-]*://[^\s/:]+:[^\s/@]+@", re.IGNORECASE),
    ),
    Rule(
        "email address",
        re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    ),
    Rule(
        "assigned secret",
        re.compile(
            r"(?i)[\"']?(?:api[_-]?key|access[_-]?token|client[_-]?secret|password|passwd)"
            r"[\"']?\s*[:=]\s*[\"'][^\"'\s]{12,}[\"']"
        ),
    ),
)

FORBIDDEN_FILENAMES = (
    re.compile(r"(^|/)\.env(?:\..+)?$"),
    re.compile(r"(^|/)(?:id_rsa|id_ed25519)$"),
    re.compile(r"\.(?:key|pem|p12|pfx)$", re.IGNORECASE),
)


def git(*arguments: str, input_bytes: bytes | None = None) -> bytes:
    return subprocess.run(
        ["git", *arguments],
        cwd=ROOT,
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout


def tracked_files() -> list[str]:
    return [item.decode() for item in git("ls-files", "-z").split(b"\0") if item]


def scan_text(label: str, content: bytes) -> list[str]:
    if len(content) > MAX_TEXT_SIZE or b"\0" in content:
        return []
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        return []
    findings: list[str] = []
    for rule in RULES:
        if rule.pattern.search(text):
            findings.append(f"{label}: {rule.name}")
    return findings


def scan_current_tree() -> tuple[list[str], int]:
    findings: list[str] = []
    files = tracked_files()
    for relative_path in files:
        if any(pattern.search(relative_path) for pattern in FORBIDDEN_FILENAMES):
            findings.append(f"{relative_path}: forbidden sensitive filename")
        findings.extend(scan_text(relative_path, (ROOT / relative_path).read_bytes()))
    return findings, len(files)


def historical_blobs() -> dict[str, str]:
    blobs: dict[str, str] = {}
    for line in git("rev-list", "--objects", "--all").decode().splitlines():
        object_id, _, path = line.partition(" ")
        if path and git("cat-file", "-t", object_id).strip() == b"blob":
            blobs.setdefault(object_id, path)
    return blobs


def scan_history() -> tuple[list[str], int]:
    findings: list[str] = []
    blobs = historical_blobs()
    for object_id, path in blobs.items():
        findings.extend(scan_text(f"history:{object_id[:12]}:{path}", git("cat-file", "blob", object_id)))
    return findings, len(blobs)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--history", action="store_true", help="scan every blob reachable from local refs")
    arguments = parser.parse_args()

    findings, file_count = scan_current_tree()
    summary = [f"current tree: {file_count} tracked files"]
    if arguments.history:
        historical_findings, blob_count = scan_history()
        findings.extend(historical_findings)
        summary.append(f"history: {blob_count} unique reachable blobs")

    if findings:
        for finding in sorted(set(findings)):
            print(f"FAIL {finding}")
        raise SystemExit(1)

    print("Publication safety scan: ok (" + "; ".join(summary) + ")")


if __name__ == "__main__":
    main()
