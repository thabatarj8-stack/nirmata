# Evidence ledger — Instagram comment to private reply

## Permission and classification

- **Project:** owner-operated Instagram comment automation.
- **Classification:** real applied case, published as a sanitized case package.
- **Source snapshot:** private repository commit `ca0ca1f9c9c51c559649af40f936a0384e7f773b`, dated 2026-08-18.
- **Client naming:** not applicable; the owner account, application name, campaign names, links, and messages are redacted.
- **Logo/screenshots:** not included.
- **Testimonial:** none.
- **Metrics permitted:** repository structure, automated test count at review time, dependency-audit result, and deterministic synthetic artifacts.
- **Sensitive details removed:** credentials, provider resource names, account handles, campaign rules, real platform identifiers, production URLs, logs, and database records.

## Claim ledger

| Proposed claim | Evidence/source | Permission | Confidence | Publish wording |
|---|---|---|---|---|
| The workflow was rebuilt as an owner-operated service | Private source tree, architecture, deployment configuration, and operational documentation | Yes, sanitized | Certain | The case documents an owner-operated replacement for one paid automation workflow |
| Webhooks are authenticated | HMAC-SHA256 implementation plus signature tests | Yes | Certain | The implementation verifies signed webhook payloads before processing |
| Duplicate comment processing is reserved in persistent storage | PostgreSQL store implementation and local store regression test | Yes | Certain for implementation; not long-term operation | The implementation reserves comment identifiers before sending and stores delivery states |
| A real external comment triggered both replies | Private operational case record dated 2026-08-18 | Yes, summarized | Likely; no raw public artifact | The private operational record reports one successful external end-to-end test |
| The system has zero recurring cost | Private case record and free-tier architecture | Yes, qualified | Time-dependent | The design targeted zero recurring platform fees within the providers' free-tier limits at the time |
| The snapshot passes its automated suite | `npm test` on the source snapshot during review | Yes | Certain | Fourteen automated tests passed on 2026-08-27 |
| Dependencies had no known audit findings | `npm audit` on the locked dependency tree during review | Yes | Certain for that audit time | The package audit reported zero known vulnerabilities on 2026-08-27 |
| No secrets exist anywhere in history | Targeted history scan; no specialist scanner was available | No strong proof | Unsupported | Do not claim; state only that the targeted scan found placeholders and no recognized live credential |
| The service is durable and reliable | No public SLA, load test, queue evidence, or long observation window | No | Unsupported | Do not claim |

## Case structure

- **One-line outcome:** an owner-operated service reproduced one comment-to-private-reply workflow and made its controls and operational trade-offs inspectable.
- **Context:** an expiring SaaS subscription threatened continuity of a small automation.
- **Challenge:** retain the essential flow while avoiding a new recurring platform fee.
- **Constraints:** official APIs, explicit publication authorization, minimal storage, free-tier infrastructure, and no public disclosure of production credentials or campaign data.
- **Approach:** signed webhook intake, deterministic rules, persistent reservation, separate external sends, health checks, and failure-preserving review.
- **Solution:** Node.js service, official platform API, hosted runtime, and PostgreSQL storage.
- **Deliverables:** private implementation and tests; public architecture, synthetic trajectory, evidence ledger, and limitations.
- **Verified outcome:** code and test evidence are public only through this sanitized record; one production success remains supported by a private operational record.
- **Next step:** add durable queueing/retry, privacy-safe logging, and a longer operational observation window.

## Publication gate

- [x] Classification is explicit.
- [x] Every numeric statement has a source and date.
- [x] Private data and production identifiers are removed.
- [x] No client identity, logo, screenshot, or testimonial is used.
- [x] Summary and detailed copy use the same evidence boundary.
