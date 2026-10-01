#!/usr/bin/env python3
"""Fail when CITATION.cff, .zenodo.json, and codemeta.json disagree.

Zenodo reads .zenodo.json instead of CITATION.cff when both exist, so a
field updated in only one file would be archived with stale metadata.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ORCID_PREFIX = "https://orcid.org/"
SPDX_PREFIX = "https://spdx.org/licenses/"


def compare(failures: list[str], field: str, expected: object, actual: object, source: str) -> None:
    if expected != actual:
        failures.append(f"{field}: CITATION.cff has {expected!r}, {source} has {actual!r}")


def main() -> int:
    citation = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
    zenodo = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
    codemeta = json.loads((ROOT / "codemeta.json").read_text(encoding="utf-8"))

    licenses = list(citation.get("license") or [])
    authors = [
        (f"{a['family-names']}, {a['given-names']}", a.get("orcid", "").removeprefix(ORCID_PREFIX))
        for a in citation["authors"]
    ]
    failures: list[str] = []

    compare(failures, "title", citation["title"], zenodo.get("title"), ".zenodo.json")
    compare(failures, "keywords", citation.get("keywords"), zenodo.get("keywords"), ".zenodo.json")
    compare(
        failures,
        "creators",
        authors,
        [(c.get("name"), c.get("orcid", "")) for c in zenodo.get("creators", [])],
        ".zenodo.json",
    )
    if zenodo.get("license", "").lower() not in {name.lower() for name in licenses}:
        failures.append(f"license: .zenodo.json has {zenodo.get('license')!r}, not one of CITATION.cff {licenses!r}")

    compare(failures, "version", str(citation["version"]), codemeta.get("version"), "codemeta.json")
    compare(failures, "doi", f"https://doi.org/{citation['doi']}", codemeta.get("identifier"), "codemeta.json")
    compare(
        failures,
        "license",
        licenses,
        [url.removeprefix(SPDX_PREFIX) for url in codemeta.get("license", [])],
        "codemeta.json",
    )
    compare(
        failures,
        "authors",
        [orcid for _, orcid in authors],
        [p.get("@id", "").removeprefix(ORCID_PREFIX) for p in codemeta.get("author", [])],
        "codemeta.json",
    )

    if failures:
        print("Citation metadata out of sync:", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
        return 1
    print("citation metadata sync: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
