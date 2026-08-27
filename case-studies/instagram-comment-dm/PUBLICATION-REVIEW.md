# Publication and security review

**Review date:** 2026-08-27  
**Private source snapshot:** `ca0ca1f9c9c51c559649af40f936a0384e7f773b`

## Publication decision

Publish a sanitized case package, not the production repository. The public package contains no credentials, production identifiers, campaign configuration, screenshots, logs, or database records.

## Evidence inventory

The reviewed private snapshot contains 33 tracked files: Node.js source, 14 automated tests, bilingual documentation, deployment configuration, six private automation configurations, and legal pages. The test suite passed during review. The locked dependency audit reported no known vulnerabilities at review time.

## Redaction decisions

| Source material | Public treatment | Reason |
|---|---|---|
| Owner account and application name | Replaced with generic roles | Avoid unnecessary identity and operational coupling |
| Automation keywords, links, and message templates | Omitted | Private campaign and distribution data |
| Provider resource names and production URLs | Omitted | Operational security |
| Real comment, message, account, and media identifiers | Replaced with synthetic identifiers | Personal data and platform metadata |
| Logs and database rows | Not copied | May contain identifiers, usernames, links, errors, and timestamps |
| Credentials and connection strings | Never copied | Secrets |
| Architecture and control sequence | Generalized and published | Necessary to audit the case's claims |

## Targeted secret review

- `.env` is ignored; only `.env.example` is tracked.
- Deployment secret fields use provider-managed values rather than committed values.
- A targeted scan of all six commits found placeholder credential examples and no recognized platform-token prefix, private key, or non-placeholder database credential.
- No specialist secret-scanning tool was available in the review environment; this result is not a guarantee that the history is secret-free.

## Security and reliability findings

| Finding | Consequence | Public claim adjustment | Recommended remediation |
|---|---|---|---|
| The webhook is acknowledged before work enters a durable queue | A process termination after acknowledgement can lose an event | Do not claim guaranteed delivery | Persist work before acknowledgement or enqueue it durably |
| A comment is reserved before the external sends, with no retry state machine | A failed send can remain reserved and never retry automatically | Describe deduplication, not exactly-once delivery | Add leases, retry policy, attempt count, and terminal states |
| Application logs include username, comment identifier, automation name, and link | Logs contain more personal/operational data than the minimal-storage narrative implies | Separate database minimization from logging behavior | Remove username/link, pseudonymize identifiers, and define retention |
| Public health output exposes dependency status | Observers can infer partial operational state | Describe monitoring without claiming zero information exposure | Consider internal authentication or a minimal liveness endpoint |
| Provider API behavior is represented by test doubles | Local tests cannot detect external API or permission changes | Do not claim ongoing provider compatibility | Add scheduled, consented canary checks with sanitized results |
| Free-tier hosting has no production SLA | Availability and wake-up latency remain provider-dependent | Do not claim durable production reliability | Record observation windows and define an operational fallback |

## Release gate

- [x] No production artifact was copied into the public package.
- [x] Claims were narrowed to their sources.
- [x] A synthetic trace replaces real identifiers and content.
- [x] Security and reliability gaps remain visible.
- [ ] Durable queue/retry is implemented and tested.
- [ ] Privacy-safe logging and retention are implemented and tested.
- [ ] A defined observation window supports any future reliability statement.
