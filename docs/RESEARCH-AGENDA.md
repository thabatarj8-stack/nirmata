# Research agenda

**Language:** English · [Português (Brasil)](RESEARCH-AGENDA.pt-BR.md)

## Current program

### RQ1 — Final output versus trajectory

Holding the content judgment constant, how much additional safety-relevant information does an independent trajectory evaluator provide?

**Next valid step:** construct a fresh, owner-authored blind holdout in a context that has never seen its ground truth. The previous holdout cannot be reused for confirmation.

### RQ2 — Delegated authority and control integrity

Can approval state machines resist forged identity, approval injection, content substitution, queue tampering, replay, and conflation of approval with publication authorization?

**Next valid step:** move the controller and publisher into a trusted control plane with independent credentials and OS-level isolation, then repeat adversarial tests against the deployed boundary.

### RQ3 — Cross-signal interference

When an LLM evaluator receives content and trajectory evidence jointly, can a clean signal in one channel reduce correct detection of an unsafe signal in the other?

**Status:** motivated by an integration-test observation; not started and not a confirmed finding.

### RQ4 — Generalization across agentic systems

Does a trajectory-aware evaluator retain useful discrimination across content publishing, browser automation, infrastructure changes, and customer-operation workflows?

**Next valid step:** define a shared minimal trajectory schema and collect matched cases from independent systems.

## Dataset growth path

1. Pilot: approximately 12 matched traces.
2. Expanded pilot: 50 traces across multiple failure classes.
3. Multi-system study: 100+ traces from independently implemented agents.
4. External replication: release a frozen evaluator and invite third-party trace submissions.

Dataset growth must not reuse burned holdouts as confirmatory evidence.

## Publication path

1. Public methods and protocol release.
2. Versioned dataset and evaluator release.
3. DOI-backed archival snapshot through Zenodo or an equivalent repository.
4. Short methods/preprint paper with explicit limitations.
5. External replication and reviewer-authored adversarial cases.
