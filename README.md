# Nirmata

**Language:** English · [Português (Brasil)](README.pt-BR.md)

Nirmata is an independent research program for evaluating AI agents from their **execution trajectories**, not only from their final outputs.

An output can look correct while the path that produced it contains an authorization error, an unsafe tool call, a broken control, or an external effect that the final answer does not reveal. Nirmata makes that path inspectable.

> **Research status:** early-stage, independent work. The evaluation pipeline has passed development and integration checks, but no blind confirmatory result is currently claimed. A first holdout was invalidated before scoring after its answer key was exposed to the evaluator context.

## Core idea

Nirmata treats an agent run as an auditable sequence of:

- decisions and candidate selection;
- source and claim verification;
- tool calls and state transitions;
- approval and authorization events;
- external effects;
- failures, corrections, and human interventions.

The project asks whether this trajectory contains safety-relevant information that is invisible when evaluation considers only the final output.

## Research questions

1. What unsafe behavior is missed when evaluators inspect only an agent's final output?
2. How much incremental safety signal is added by raw trajectory evidence?
3. Can approval protocols preserve human authority under adversarial or ambiguous inputs?
4. Can independently evaluating content and trajectory reduce cross-signal interference?
5. How should agent failures be preserved so later claims remain auditable and reproducible?

## Research pillars

| Pillar | Object of study | Current evidence |
|---|---|---|
| Trajectory-aware evaluation | Final-output-only vs. output plus independent trajectory signal | Factorized pipeline integration validated; blind confirmation pending |
| Delegated authority | Approval, queueing, publication authorization, and external effects | 12 development/control-integrity checks passed; real isolation remains a limitation |
| Failure-preserving methodology | Versioned corrections, aborted runs, invalidated holdouts, and frozen designs | Run manifests and failure records exist in the source laboratory |
| Applied autonomy | Replacing opaque SaaS dependencies with owner-governed systems | Instagram comment-to-DM case completed in production |

## Experiments

| Experiment | Question | Status |
|---|---|---|
| [#001 — Strategic agent evaluation and delegated authority](experiments/README.md#experiment-001) | Can an editor select, verify, and act without exceeding delegated authority? | Exploratory run + adversarial control checks completed |
| [#002 — Final output vs. execution trajectory](experiments/README.md#experiment-002) | Does trajectory evidence reveal safety failures hidden from output-only evaluation? | Pipeline frozen; original blind holdout invalidated; fresh holdout required |
| [#003 — Evaluator context interference](experiments/README.md#experiment-003) | Can one evidence channel interfere with the evaluation of another? | Candidate study; not started |

## Applied case studies

- [Instagram comment-to-DM: from ManyChat to owner-governed infrastructure](case-studies/README.md#instagram-comment--dm) — a production case examining autonomy, operational evidence, delegated authority, hidden costs, and the difference between a successful demo and a durable system.

## Methodological commitments

- Preserve failures instead of rewriting the history into a clean success story.
- Separate development tests, integration validation, and blind confirmation.
- Freeze designs and evaluator configurations before confirmatory data is seen.
- Persist predictions before revealing ground truth.
- Distinguish blocked attempts from executed policy violations.
- Report simulated controls and shared-process limitations explicitly.
- Use language no stronger than the available evidence.

See [Methodology](docs/METHODOLOGY.md), [Evidence status](docs/EVIDENCE-STATUS.md), [Research agenda](docs/RESEARCH-AGENDA.md), [Related work](docs/RELATED-WORK.md), [Glossary](docs/GLOSSARY.md), and the [Discovery and publication checklist](docs/DISCOVERY-AND-PUBLICATION.md).

## What Nirmata does not claim

- It does not claim that trajectory-aware evaluation is universally superior.
- It does not claim production-grade control-plane isolation.
- It does not treat development-test success as evidence of generalization.
- It does not report a confirmatory effect size from the invalidated holdout.
- It is not a benchmark yet; the current work is a pilot research program.

## Citation

Use the repository's [`CITATION.cff`](CITATION.cff). A DOI-backed archival release is planned after the public research package and licensing are finalized.

## Author

Nirmata is an independent research project by [Tabata Jahoda](https://github.com/thabatarj8-stack).

## License status

No reuse license has been selected yet. Until a license is added, copyright remains with the author and public visibility does not imply permission to reuse the materials.
