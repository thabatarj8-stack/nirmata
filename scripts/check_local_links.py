#!/usr/bin/env python3
"""Fail when a relative Markdown link points to a missing local file."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    failures: list[str] = []
    for markdown_file in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown_file.parts:
            continue
        for target in LINK.findall(markdown_file.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            file_part = unquote(target.split("#", 1)[0])
            if file_part and not (markdown_file.parent / file_part).resolve().exists():
                failures.append(f"{markdown_file.relative_to(ROOT)} -> {target}")
    if failures:
        print("Missing local Markdown targets:", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
        return 1
    print("local Markdown links: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
