# Nirmata

Nirmata is an open research framework for auditing AI agents by what they actually do, not only by what they say.

**Current version:** `v0.1.0` · [Release contents](releases/v0.1.0/README.md) · [Brazilian Portuguese](README.pt-BR.md)

**Project site:** MkDocs Material sources live in [`website/`](website/index.md). [GitHub Actions](.github/workflows/pages.yml) deploys the site when Pages is set to GitHub Actions.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22132451.svg)](https://doi.org/10.5281/zenodo.22132451)
[![Code license: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSES/Apache-2.0.txt)
[![Docs license: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey.svg)](LICENSES/CC-BY-4.0.txt)

> **Evidence status of the v0.1.0 package:** early-stage pilot. Development and integration checks have passed. No blind confirmatory result is claimed for that package. The first planned Experiment 002 holdout was invalidated before scoring because its answer key entered the evaluator context. [Evidence ledger](docs/EVIDENCE-STATUS.md).

## Why it matters

When an agent uses tools, changes state, or acts in an external system, a plausible final answer is incomplete evidence. The execution path may contain an authorization error, a blocked attack, a broken control, or an effect that the answer never mentions.

Nirmata keeps those facts distinct:

- A recommendation, reviewer opinion, queue state, or earlier approval is not owner authorization. Authorization is recorded separately from the requested action. See [Approval is not authorization](articles/en/approval-is-not-authorization.md) and the [trace schema](docs/experimental-standard/v0.1/TRACE-SCHEMA.md).
- An attempt is not an effect. A blocked unauthorized request (`UNAUTHORIZED_ATTEMPT_BLOCKED`) is not the same event as an executed policy violation or a harmful external effect. See [Methodology](docs/METHODOLOGY.md).
- Two evaluators stay independent. A **content evaluator** sees only the final output. A **trajectory evaluator** sees only process evidence. A deterministic rule combines them: `unsafe = content_unsafe OR trajectory_unsafe`. A clean signal in one channel cannot erase an unsafe signal in the other. See [Experiment 002 protocol](experiments/002/protocol/protocol-v1.0.md).

The public executable baseline in `reproducibility/` is a deterministic stand-in for that two-channel design. It uses visible synthetic markers. It checks plumbing. It is not a model score and not confirmatory evidence.

Integrity in this repository is SHA-256 on the fields the published schemas actually define. The executable schema requires `final_output.content_hash`, and `reproducibility/scripts/validate.py` rejects a mismatch. The experimental standard also asks, where available, for hashes of inputs, outputs, approved content, and state before and after a transition. Run manifests record hashes of inputs and outputs. [Methodology](docs/METHODOLOGY.md) states the limit directly: tamper detection is conditional on execution still passing through a trusted verifier.

## Four phases

[ROADMAP.md](ROADMAP.md) orders the program by evidentiary dependency. These are the four phases as written there.

### Phase 1 — Reproducibility foundation

- [x] Publish a minimal trajectory schema.
- [x] Publish synthetic calibration traces and expected classifications.
- [x] Provide deterministic validation, evaluation, scoring, manifests, and tests.
- [x] Run documentation and pipeline checks in continuous integration.
- [ ] Invite external review of the schema and process taxonomy.

### Phase 2 — Release candidate

- [x] Publish a sanitized applied-case package without production artifacts.
- [x] Review every public artifact for secrets, identifiers, client material, and holdout leakage ([audit](docs/PUBLICATION-AUDIT-2026-08-27.md)).
- [x] Add ORCID to citation and project metadata.
- [x] Freeze a `v0.1.0` release candidate and record artifact hashes ([release record](releases/v0.1.0/README.md)).
- [x] Connect GitHub to Zenodo and archive the release with a DOI ([10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451)).

### Phase 3 — Fresh blind pilot

- [ ] Pre-register the frozen protocol and primary metrics.
- [ ] Assign independent custody of new holdout labels.
- [ ] Persist and hash predictions before ground-truth release.
- [ ] Score without changing prompts, rubrics, thresholds, or cases.
- [ ] Publish positive, negative, partial, or invalidated outcomes.

### Phase 4 — External validity

- [ ] Add independently authored adversarial traces.
- [ ] Replicate on at least one separately implemented agentic system.
- [ ] Compare the taxonomy formally with adjacent benchmarks and assurance methods.
- [ ] Prepare a methods note only after the public artifacts support it.

## Quickstart

The public calibration package uses the Python 3 standard library only. From a checkout of this repository:

```bash
python3 reproducibility/scripts/validate.py
python3 reproducibility/scripts/baseline.py \
  --output reproducibility/runs/example/predictions.jsonl \
  --manifest reproducibility/runs/example/manifest.json
python3 reproducibility/scripts/score.py \
  --predictions reproducibility/runs/example/predictions.jsonl \
  --report reproducibility/runs/example/score-report.json
python3 -m unittest discover -s reproducibility/tests -v
python3 scripts/check_local_links.py
```

`validate.py` exits 0 and prints `status: ok` with 6 calibration traces, 6 labels, and 1 applied trace. The score report's `claim_boundary` says the fixture is not model performance and not confirmatory evidence. Details: [reproducibility package](reproducibility/README.md).

To check the frozen `v0.1.0` archive hashes, export that tag and run the checksum file from inside it. On current `main`, the same check does not apply: files changed after the tag when the DOI was published.

```bash
mkdir -p /tmp/nirmata-v0.1.0
git archive v0.1.0 | tar -x -C /tmp/nirmata-v0.1.0
( cd /tmp/nirmata-v0.1.0 && shasum -a 256 -c releases/v0.1.0/SHA256SUMS )
```

Continuous integration also validates Experiment 002 JSON Schemas after installing `jsonschema==4.25.1`. That step is in [`.github/workflows/quality.yml`](.github/workflows/quality.yml). It is not part of the dependency-free package above.

## Results

The published n8n adapter evaluation is [HOLDOUT_REPORT.md](research/m2/evaluation/n8n/run_002/HOLDOUT_REPORT.md).

`HOLDOUT_PASS = true` on eight preregistered criteria. The report treats the pass as all-or-nothing, and all eight criteria are true. Its allowed conclusion is:

> n8n Adapter v0.1.0 demonstrated within-scope holdout generalization on a second preregistered synthetic n8n workflow that was not used for adapter implementation.

That report does not claim that the adapter generalizes to n8n, that it is production-ready, that it supports arbitrary n8n workflows, or that Nirmata is validated across orchestrators. Proposal 005 remains open and still requires M2 evidence. The result does not prove source authenticity. Original evidence remains outside Git. The commit hashes cited in the report live in a private development repository; the report is published here for transparency.

This result does not close Phase 3 in [ROADMAP.md](ROADMAP.md). Those items are still open. The [evidence ledger](docs/EVIDENCE-STATUS.md) for the `v0.1.0` package still records no confirmatory result, including the invalidated first Experiment 002 holdout.

## How to contribute

Issues and pull requests are welcome. Failures, negative results, partial outcomes, aborted runs, and invalidated holdouts belong in the record. Do not rewrite them into a success story, and do not drop them.

- Open a [research task](.github/ISSUE_TEMPLATE/research-task.yml) or a [replication report](.github/ISSUE_TEMPLATE/replication.yml). The replication template asks for successful, failed, partial, and aborted outcomes, plus every known protocol deviation.
- Read [CONTRIBUTING.md](CONTRIBUTING.md) before a pull request. Label work as exploratory, development, integration, confirmatory, or invalidated.
- Report credentials, private traces, or unpublished holdout answers through the process in [SECURITY.md](SECURITY.md), not in a public issue.

Do not submit secrets, client data, access tokens, or proprietary traces.

## How to cite

Version `v0.1.0` is archived at [doi:10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451). The concept DOI for all Nirmata versions is `10.5281/zenodo.22132450`.

> Jahoda, Tabata. *Nirmata: Trajectory-Aware Evaluation and Delegated Authority for AI Agents*. Version 0.1.0. [10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451)

Machine-readable metadata is in [`CITATION.cff`](CITATION.cff). ORCID: [0009-0007-1104-9204](https://orcid.org/0009-0007-1104-9204).

Code is Apache-2.0. Documentation, protocols, taxonomies, diagrams, articles, and public datasets are CC BY 4.0. See [LICENSE.md](LICENSE.md).

## Repository map

```text
articles/          Essays in English and Brazilian Portuguese
case-studies/      Applied operational cases
docs/              Method, evidence ledger, agenda, experimental standard
experiments/       Registry, Experiment 002 protocol, schemas, templates
reproducibility/   Executable schema, synthetic traces, baseline, scoring, tests
releases/v0.1.0/   Frozen release record and SHA256SUMS
research/m2/       Published n8n adapter holdout report
```

## Author

Nirmata is independent research by [Tabata Jahoda](https://github.com/thabatarj8-stack). [LinkedIn](https://www.linkedin.com/in/tabata-j-226b6123/).

## Support this research

Nirmata is independent, open research (Apache-2.0). The next step is a
preregistered blind pilot comparing output-only and trajectory-aware evaluation
of AI agents, followed by a replication. Results will be published whatever
the outcome, including null or negative results.

There is no confirmatory result yet. The current release ships the schema,
protocols and a reproducible fixture of 6 traces with tests.

The pilot is crowdfunding on Manifund until 26 Nov 2026
(US$3k minimum, US$14.2k goal):
<https://manifund.org/projects/nirmata-auditing-ai-agents-by-what-they-do-not-only-what-they-say>

Other ways to help:

- Critique the trace schema or the evaluation protocol by opening an issue.
- Share real or synthetic agent workflows that could become test traces.
- Cite the release: <https://doi.org/10.5281/zenodo.22132451>
