# Nirmata Publication Safety v0.1

**Status:** Draft

## Minimum Necessary Disclosure Principle

Public research artifacts should expose only the information necessary to reproduce or audit the scientific claim.

Public releases should remove, generalize, or replace information that is unnecessary to the claim, including:

- personal names;
- usernames and handles;
- customer or client identities;
- private organization identifiers where unnecessary;
- email addresses and phone numbers;
- account and resource identifiers that can be mapped to real subjects;
- API keys, access tokens, credentials, secrets, and session identifiers;
- webhook secrets;
- private URLs and internal infrastructure paths;
- private communications unless indispensable to the scientific claim;
- commercially sensitive operational information.

Use synthetic identifiers such as `ACTOR-01`, `OWNER`, `ORG-A`, `SYSTEM-A`, and `RESOURCE-001`.

## Evidence layers

Nirmata distinguishes raw evidence from public research artifacts:

```text
RAW / PRIVATE EVIDENCE
        |
        v
sanitization + semantic verification
        |
        v
PUBLIC RESEARCH ARTIFACT
```

Sanitization must not alter safety-relevant semantics. If removing a field would change the meaning of an authorization path, state transition, or external effect, preserve the relevant relationship while replacing identifying values with synthetic equivalents.

## Timing

For confirmatory datasets, sanitization should occur before the evaluator-facing dataset is frozen and hashed. A separately retained raw artifact may remain private when required for provenance or audit.

## Secrets

Secrets and credentials must never be committed to the public repository, including in examples, test fixtures, logs, commit messages, issue bodies, or pull-request descriptions.

## Publication review

Before any evidence artifact becomes public, verify that it contains no unnecessary identity data, credentials, private communications, or operational details that increase risk without increasing scientific auditability.