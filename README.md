# Nirmata

**Language:** English · [Português (Brasil)](README.pt-BR.md)

**Nirmata is an independent research program that evaluates AI agents from what they do—not only from what they say.**

**Current version:** `v0.1.0` · [Release contents and verification](releases/v0.1.0/README.md)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22132451.svg)](https://doi.org/10.5281/zenodo.22132451)

When an agent uses tools, changes state, or acts in an external system, a plausible final answer is incomplete evidence. The execution path may contain an authorization error, a blocked attack, a broken control, or an effect that the answer never mentions. Nirmata makes that path inspectable and keeps failed evaluations in the research record.

> **Evidence status:** early-stage pilot. Development and integration checks have passed, but no blind confirmatory result is claimed. The first planned holdout was invalidated before scoring because its answer key entered the evaluator context. [See the evidence ledger.](docs/EVIDENCE-STATUS.md)

## Start here

| If you want to... | Read... |
|---|---|
| Understand the idea in five minutes | [Why final answers are not enough](articles/en/why-final-answers-are-not-enough.md) |
| Inspect the evaluation design | [Methodology](docs/METHODOLOGY.md) |
| Inspect the versioned operational contracts | [Experimental Standard v0.1](docs/experimental-standard/v0.1/README.md) |
| Run the public calibration fixture | [Reproducibility package](reproducibility/README.md) |
| Check what the evidence does and does not support | [Evidence status](docs/EVIDENCE-STATUS.md) |
| Review the experiment history | [Experiment registry](experiments/README.md) |
| See the practical relevance | [Applied case studies](case-studies/README.md) |
| Replicate, challenge, or contribute | [Roadmap](ROADMAP.md) · [Research agenda](docs/RESEARCH-AGENDA.md) · [Contributing](CONTRIBUTING.md) |

## The evaluation model

Nirmata separates two signals that are often mixed together:

1. A **content evaluator** judges only the final output.
2. A **trajectory evaluator** judges raw process evidence such as tool calls, authorization events, state transitions, and external effects.
3. A deterministic rule combines both judgments without allowing a clean signal to erase an unsafe one.

```text
Final-only:        unsafe = content_unsafe
Trajectory-aware: unsafe = content_unsafe OR trajectory_unsafe
```

This is a research design under evaluation, not a claim that trajectory-aware evaluation is universally superior.

## Research program

| Workstream | Question | Current status |
|---|---|---|
| Final output vs. trajectory | What safety-relevant behavior is invisible in the final answer? | Factorized pipeline integrated; fresh blind holdout required |
| Delegated authority | Can an agent act without conflating advice, approval, queueing, and publication? | 12 known development/control checks passed; real isolation pending |
| Evaluator interference | Can one evidence channel distort judgment of another? | Candidate study; not started |
| Applied autonomy | What does operational ownership expose that a successful demo hides? | One production case documented; long-term reliability not established |

The [experiment registry](experiments/README.md) records exploratory, development, integration, invalidated, and future confirmatory work separately.

## Articles

- [Why final answers are not enough to evaluate AI agents](articles/en/why-final-answers-are-not-enough.md)
- [Approval is not authorization in agentic systems](articles/en/approval-is-not-authorization.md)
- [A burned holdout is still research evidence](articles/en/a-burned-holdout-is-still-evidence.md)
- [All articles in English and Portuguese](articles/README.md)

## Research principles

- Preserve failures instead of rewriting them into a clean success story.
- Separate development tests, integration validation, and blind confirmation.
- Freeze designs and evaluator configurations before confirmatory data is seen.
- Persist predictions before revealing ground truth.
- Distinguish blocked attempts from executed policy violations.
- Match every public statement to the strength of its evidence.

## Scope and limitations

Nirmata is a pilot research program and case laboratory. It is not yet a benchmark, a production security product, or proof that its evaluation design generalizes. Current cases are small and domain-specific; identity attestation and control isolation remain prototype limitations. See [Methodology](docs/METHODOLOGY.md), [Related work](docs/RELATED-WORK.md), and [Research agenda](docs/RESEARCH-AGENDA.md).

## Repository map

```text
articles/       Accessible essays in English and Portuguese
case-studies/   Applied operational cases
docs/           Method, evidence ledger, literature map, agenda, and experimental standard
experiments/    Experiment registry, protocols, schemas, and status
reproducibility/ Schema, synthetic traces, evaluator, scoring, and tests
```

## Citation and license

Use [`CITATION.cff`](CITATION.cff) to cite the project. Version `v0.1.0` is archived at [DOI 10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451).

Software, when published here, is licensed under Apache-2.0. Documentation, protocols, taxonomies, diagrams, articles, and public datasets are licensed under CC BY 4.0. See [LICENSE.md](LICENSE.md).

## Author

Nirmata is independent research by [Tabata Jahoda](https://github.com/thabatarj8-stack), [ORCID 0009-0007-1104-9204](https://orcid.org/0009-0007-1104-9204). Connect on [LinkedIn](https://www.linkedin.com/in/tabata-j-226b6123/).
