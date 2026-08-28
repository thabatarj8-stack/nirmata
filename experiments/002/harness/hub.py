#!/usr/bin/env python3
"""Hugging Face Hub custody for the H2 holdout.

The seals in blinding.py prove integrity to us. This module adds the part a
local seal cannot provide: an external, timestamped witness that predictions
were committed before the key was published.

Custody model, two separate dataset repos:

  <namespace>/nirmata-002-h2-traces   evaluator-facing traces, private then gated
  <namespace>/nirmata-002-h2-key      sealed ground truth, private until reveal

Separate repos rather than branches, because a wrong repo_id is a visible typo
while a wrong revision is silent. The evaluator context should hold a token
scoped to the traces repo only.

This is the only module in the harness that needs a network or a third-party
dependency. Nothing here runs unless it is called explicitly.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

HARNESS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(HARNESS_DIR))
from blinding import read_seal, require, sha256_file, verify_seal  # noqa: E402

TRACES_SUFFIX = "nirmata-002-h2-traces"
KEY_SUFFIX = "nirmata-002-h2-key"


def api() -> Any:
    from huggingface_hub import HfApi

    return HfApi()


def repo_ids(namespace: str) -> dict[str, str]:
    return {"traces": f"{namespace}/{TRACES_SUFFIX}", "key": f"{namespace}/{KEY_SUFFIX}"}


def create_custody_repos(namespace: str, *, dry_run: bool = True) -> dict[str, Any]:
    """Create both dataset repos as private. Publication is a separate, later act."""
    ids = repo_ids(namespace)
    if dry_run:
        return {"dry_run": True, "would_create": [f"dataset:{value} (private)" for value in ids.values()]}
    client = api()
    created = {}
    for role, repo_id in ids.items():
        info = client.create_repo(repo_id=repo_id, repo_type="dataset", private=True, exist_ok=True)
        created[role] = str(info)
    return {"dry_run": False, "created": created}


def push(
    local_path: Path,
    repo_id: str,
    *,
    path_in_repo: str,
    message: str,
    dry_run: bool = True,
) -> dict[str, Any]:
    """Upload one file and return the commit that now witnesses it."""
    require(local_path.is_file(), f"nothing to push: {local_path}")
    digest = sha256_file(local_path)
    if dry_run:
        return {
            "dry_run": True,
            "would_push": str(local_path),
            "repo_id": repo_id,
            "path_in_repo": path_in_repo,
            "sha256": digest,
        }
    commit = api().upload_file(
        path_or_fileobj=str(local_path),
        path_in_repo=path_in_repo,
        repo_id=repo_id,
        repo_type="dataset",
        commit_message=message,
    )
    return {
        "dry_run": False,
        "repo_id": repo_id,
        "path_in_repo": path_in_repo,
        "sha256": digest,
        "commit_url": getattr(commit, "commit_url", None),
        "commit_oid": getattr(commit, "oid", None),
    }


def pull_pinned(repo_id: str, *, filename: str, revision: str, dest_dir: Path) -> Path:
    """Download one file at an immutable revision. Never accepts a branch name."""
    require(
        not repo_id.endswith(KEY_SUFFIX),
        "refusing to pull the key repo through the evaluator-facing path",
    )
    require(
        len(revision) == 40 and all(char in "0123456789abcdef" for char in revision.lower()),
        f"revision must be a full 40-character commit sha, got {revision!r}",
    )
    from huggingface_hub import hf_hub_download

    dest_dir.mkdir(parents=True, exist_ok=True)
    path = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        repo_type="dataset",
        revision=revision,
        local_dir=str(dest_dir),
    )
    return Path(path)


def verify_against_seal(seal_path: Path, directory: Path) -> dict[str, Any]:
    """Confirm that what came back from the Hub is byte-identical to what was sealed."""
    record = read_seal(seal_path)
    verify_seal(record, directory)
    return {"status": "verified", "stage": record["stage"], "sealed_at": record["sealed_at"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--namespace", required=True, help="Hub user or org, e.g. Nirmata-88")
    parser.add_argument("--create", action="store_true", help="create the two private dataset repos")
    parser.add_argument("--execute", action="store_true", help="actually call the Hub (default is dry run)")
    args = parser.parse_args()
    try:
        if args.create:
            result = create_custody_repos(args.namespace, dry_run=not args.execute)
        else:
            result = {"repos": repo_ids(args.namespace)}
    except (OSError, ValueError) as error:
        print(f"hub action failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
