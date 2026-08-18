# Applied case studies

## Instagram comment → DM

**Question:** Can a paid ManyChat comment-to-DM automation be replaced by owner-governed infrastructure without giving up security controls, auditability, and a zero recurring platform-cost target within free-tier limits?

**System:** Meta Webhooks and Instagram Graph API, a Node.js service, Render hosting, and Neon PostgreSQL.

**Observed outcome:** A real external Instagram account triggered a public reply and a private reply. The deployed system includes signed-webhook validation, persistent comment deduplication, separate status tracking for public/private sends, and health checks for the database and Meta token.

**Nirmata relevance:** The trajectory captured properties that a successful demo did not reveal: ephemeral SQLite storage, secret synchronization risk, shared Meta permissions, publication prerequisites, authorization boundaries, and the transfer of operational responsibility from SaaS vendor to owner.

**Limitations:** Free tiers provide no production SLA; APIs and tokens require maintenance; zero monetary subscription cost does not mean zero operational cost.

The production repository remains private while its public-release security review is pending.
