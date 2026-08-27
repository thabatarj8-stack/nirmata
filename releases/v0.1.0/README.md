# Nirmata v0.1.0 release candidate

**Freeze date:** 2026-08-27

**Evidence status:** early-stage pilot; no blind confirmatory result claimed

## Contents

This release candidate freezes the first auditable public Nirmata research package:

- the trajectory-aware evaluation method and evidence ledger;
- the versioned Experimental Standard v0.1;
- the Experiment 002 protocol, evaluator contracts, schemas, and synthetic prediction templates;
- the executable calibration and scoring pipeline;
- a sanitized applied automation case;
- three bilingual research articles;
- citation, licensing, security, and contribution metadata.

## Evidence boundary

The executable fixtures establish package integrity and expected behavior on known synthetic cases. They do not establish evaluator generalization, production security, or a successful blind confirmatory result. The fresh Experiment 002 holdout remains future work.

## Integrity verification

`SHA256SUMS` records every tracked release file except the checksum file itself. From a checkout of the release commit or tag, run:

```bash
shasum -a 256 -c releases/v0.1.0/SHA256SUMS
```

The release was prepared only after the reproducibility suite, JSON Schema validation, local-link checks, Markdown lint, and publication-safety scan passed.

## Archival status

GitHub release publication and DOI archival are intentionally pending until the repository is enabled in the Zenodo GitHub integration. This ordering prevents publication before the archival integration is ready.

## Citation

Use the repository [`CITATION.cff`](../../CITATION.cff). Add the version-specific DOI after Zenodo finishes processing the GitHub release.
