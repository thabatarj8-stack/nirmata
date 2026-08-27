# Publication safety audit — 2026-08-27

## Decision

The tracked research package is suitable to continue toward a release candidate. No production artifact, holdout answer key, or recognized secret was found in the current tree or reachable file history. The repository owner accepted the existing author-email metadata exposure on 2026-08-27 and chose to preserve the public Git history.

## Scope

The review covered:

- every tracked file in the repository;
- every unique file blob reachable from local Git refs;
- filenames associated with environment files, private keys, and credential bundles;
- high-confidence patterns for private keys, provider tokens, credential-bearing URLs, assigned secrets, and email addresses;
- Experiment 002 holdout materials and references to ground truth;
- repository object sizes and unexpected binary or oversized artifacts;
- GitHub secret-scanning alerts available through the repository API.

The automated scan is reproducible with:

```bash
python scripts/audit_publication_safety.py --history
```

Continuous integration now runs the same check against the full reachable history.

## Findings

### Current files and historical blobs

- No recognized credential, private key, direct email address, or credential-bearing URL was detected in tracked file content.
- No sensitive filename such as a tracked `.env`, private key, or credential bundle was detected.
- Experiment 002 contains handling rules, synthetic prediction templates, and a sealed hash placeholder. It does not contain holdout traces or an answer key.
- GitHub reported no secret-scanning alerts at review time.

### Commit metadata

The author's personal email address is present in existing commit metadata, primarily in merge commits and commits created outside the locally configured GitHub no-reply identity. Commit metadata is public and is not changed by deleting content from the current tree.

Recommended actions before the release candidate:

1. Enable GitHub's private-email and command-line push protection settings for future commits.
2. Confirm whether the existing metadata exposure is acceptable.
3. If removal is required, plan a separate history rewrite with explicit coordination because every rewritten commit hash and dependent reference will change.

No history rewrite was performed during this audit.

The repository owner accepted this existing exposure on 2026-08-27. Future commits should use the configured GitHub no-reply identity; the acceptance does not imply that additional personal contact information may be published.

## Limitations

Pattern matching can detect known formats and direct identifiers, but it cannot prove the absence of every secret or infer whether every opaque identifier maps to a real subject. The applied case therefore retains its separate semantic publication review, and future evidence packages still require human review under the Minimum Necessary Disclosure Principle.

## Release gate

- [x] Current tracked files scanned.
- [x] Reachable historical file blobs scanned.
- [x] Experiment 002 checked for premature ground-truth disclosure.
- [x] GitHub secret-scanning alerts checked.
- [x] Known limitation and author-email metadata exposure documented.
- [x] Author-email metadata exposure accepted or remediated.
- [x] Release-candidate hashes generated after the final tree is frozen.
