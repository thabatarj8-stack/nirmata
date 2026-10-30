---
description: Nirmata audits AI agents by what they do, not only by what they say. v0.1.0 is an early pilot with no blind confirmatory result.
---

# Nirmata

**Version `v0.1.0`** · [DOI 10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451) · [ORCID 0009-0007-1104-9204](https://orcid.org/0009-0007-1104-9204)

> Nirmata is an open research framework for auditing AI agents by what they actually do, not only by what they say.
{: .thesis }

Independent research by [Tabata Jahoda](https://github.com/thabatarj8-stack). When an agent uses tools, changes state, or acts in an external system, a plausible final answer is incomplete evidence. The execution path may contain an authorization error, a blocked attack, a broken control, or an effect that the answer never mentions.

!!! evidence "Evidence status of the v0.1.0 package"

    Early-stage pilot. Development and integration checks have passed. **No blind confirmatory result is claimed** for that package. The first planned Experiment 002 holdout was invalidated before scoring because its answer key entered the evaluator context.

    No record in the current package is labelled confirmatory. [Open the evidence ledger](docs/EVIDENCE-STATUS.md).

## What this project does not claim {: .boundary-title }

- **v0.1.0 is an early pilot.** It does not include a blind confirmatory result.
- **The first Experiment 002 holdout was invalidated by answer-key leakage.** The answer key entered the evaluator context before scoring. That run supports no blind performance claim.
- **The reproducibility baseline is deterministic and synthetic.** It is not a model score and not confirmatory evidence.
- **Nirmata does not detect CVEs or language bugs.**

The public executable baseline in `reproducibility/` uses visible synthetic markers. It checks plumbing. The [reproducibility quickstart](reproducibility-quickstart.md) states that boundary again, next to the commands.

## How the audit is factored

Nirmata keeps these facts distinct. Wording below follows the repository README.

- A recommendation, reviewer opinion, queue state, or earlier approval is not owner authorization. Authorization is recorded separately from the requested action.
- An attempt is not an effect. A blocked unauthorized request (`UNAUTHORIZED_ATTEMPT_BLOCKED`) is not the same event as an executed policy violation or a harmful external effect.
- Two evaluators stay independent. A **content evaluator** sees only the final output. A **trajectory evaluator** sees only process evidence. A deterministic rule combines them. A clean signal in one channel cannot erase an unsafe signal in the other.

```text
unsafe = content_unsafe OR trajectory_unsafe
```

That design is not a claim that trajectory-aware evaluation is universally better. Phase 2 of the [roadmap](ROADMAP.md) is checked, including the DOI. Phase 1 still has external review of the schema and process taxonomy open. Phase 3 (fresh blind pilot) and Phase 4 (external validity) are open.

<div class="grid cards" markdown>

- [**Evidence status**](docs/EVIDENCE-STATUS.md)

  What each record supports, and the extrapolation it does not support.

- [**Roadmap**](ROADMAP.md)

  Four phases ordered by evidentiary dependency.

- [**Reproducibility quickstart**](reproducibility-quickstart.md)

  Deterministic synthetic baseline. Not a model score.

- [**Why final answers are not enough**](articles/en/why-final-answers-are-not-enough.md)

  The short essay. Claims stay inside the evidence ledger.

</div>

## How to cite

Version `v0.1.0` is archived at [doi:10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451). The concept DOI for all Nirmata versions is `10.5281/zenodo.22132450`.

> Jahoda, Tabata. *Nirmata: Trajectory-Aware Evaluation and Delegated Authority for AI Agents*. Version 0.1.0. [10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451)

Machine-readable metadata is in [`CITATION.cff`](CITATION.cff). ORCID: [0009-0007-1104-9204](https://orcid.org/0009-0007-1104-9204).

Code is Apache-2.0. Documentation, protocols, taxonomies, diagrams, articles, and public datasets are CC BY 4.0.

## A published result, and its limit

The published n8n adapter evaluation is [HOLDOUT_REPORT.md](research/m2/evaluation/n8n/run_002/HOLDOUT_REPORT.md). `HOLDOUT_PASS = true` on eight preregistered criteria. The report treats the pass as all-or-nothing, and all eight criteria are true. Its allowed conclusion is:

> n8n Adapter v0.1.0 demonstrated within-scope holdout generalization on a second preregistered synthetic n8n workflow that was not used for adapter implementation.

That report does not claim that the adapter generalizes to n8n, that it is production-ready, that it supports arbitrary n8n workflows, or that Nirmata is validated across orchestrators. This result does not close Phase 3. The evidence ledger for the `v0.1.0` package still records no confirmatory result, including the invalidated first Experiment 002 holdout.

## Support this research

Nirmata is independent, open research (Apache-2.0). The next step is a preregistered blind pilot comparing output-only and trajectory-aware evaluation of AI agents, followed by a replication. Results will be published whatever the outcome, including null or negative results.

There is no confirmatory result yet. The current release ships the schema, protocols and a reproducible fixture of 6 traces with tests.

The pilot is crowdfunding on [Manifund](https://manifund.org/projects/nirmata-auditing-ai-agents-by-what-they-do-not-only-what-they-say). The current deadline and amounts are on that page.
