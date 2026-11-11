# Working on Nirmata

Repository instructions, reviewed against `main` at `583f55e2c708135fd275e120a167e7e88920a5cd` on 2026-11-11. These instructions do not themselves authorize publication, external actions, expenditure, or a holdout run.

## Purpose and evidence

Nirmata studies trajectory-aware evaluation, delegated authority, control integrity, and failure-preserving reproducibility. Read `README.md`, `CONTRIBUTING.md`, `docs/METHODOLOGY.md`, `docs/EVIDENCE-STATUS.md`, and `SECURITY.md` before contributing.

- Label work as exploratory, development, integration, confirmatory, or invalidated. Explain the evidence supporting the label.
- The six public calibration cases and deterministic baseline in `reproducibility/` are an integration fixture. They do not measure model performance or establish generalization or production safety.
- Preserve failed, negative, partial, aborted, and invalidated outcomes. Do not replace the first Experiment 002 holdout's invalidation with a success narrative.
- The published n8n run_002 report supports a narrow normalization-fidelity claim on one synthetic workflow. Its private development commits and original evidence are not a publicly executable replication package. Do not turn that report into failure-detection accuracy or general Nirmata validation.
- Distinguish what was inspected, what was executed, and what was independently reproduced. A passing check is evidence only for the behavior it exercised.

## Before starting

1. Record the exact commit, clean/dirty working-tree state, task, intended evidence class, and expected output. Read any more specific repository instructions.
2. Check existing issues and PRs. Do not duplicate schema review issue #4 or blind-pilot issue #6. At the review date, PR #15 proposes a blinding harness and PR #16 proposes metadata changes; both remain open. PR #24 is merged and corrects the public baseline's label-access documentation. Recheck current state rather than treating proposed PR content as `main` or reopening completed work.
3. Keep one task or scientific question per change. State inputs, acceptance criteria, dependencies, budget, stop conditions, and exclusions before execution.
4. Use a separate branch or disposable local copy when changes are authorized. Do not overwrite an archived release, existing run artifacts, or another contributor's work.
5. A request for preparation or review does not authorize publishing issues, comments, branches, PRs, releases, external messages, or uploads. Obtain the appropriate approval for those actions. Keep approved publication within its reviewed scope.

## Keep the contracts separate

- `reproducibility/schema/trajectory.schema.json` describes the public fixture: lowercase `trajectory_id`, `type`, and `outcome` fields.
- `experiments/002/schemas/trace.schema.json` describes Experiment 002: `trace_id` in the `NIR-002-*` family and `event_type`, with different authorization and effect fields.
- Do not silently cast, rename, merge, or reuse validators across these contracts. Any migration needs an explicit mapping, version, loss accounting, and tests.
- Preserve the evaluation boundary: content uses final output; trajectory uses allowed process evidence; deterministic aggregation is `content_unsafe OR trajectory_unsafe`.
- An approval, reviewer recommendation, or queue state is not owner authorization. A blocked attempt is not an executed violation. An observed action is not proof of its external effect. Missing evidence must not become a fabricated safe state.

## Holdout boundary

Read `docs/experimental-standard/v0.1/BLINDING-PROTOCOL.md`, `experiments/002/holdout/README.md`, and `experiments/002/PRE-RUN-CHECKLIST.md` before work touching Experiment 002.

- Public review and regression work uses existing public calibration material or explicitly disposable synthetic development cases. Never request or search for the fresh holdout answer key for these tasks.
- Keep fresh labels and rationales outside this public repository and technically inaccessible to evaluator contexts. A different filename or directory alone is not access isolation.
- Case author, custodian, evaluator, and scorer are distinct information roles. Record which material each role has seen. Do not assign a label-exposed context to blind evaluation of those same cases.
- Freeze protocol, case definition, prompts, exact available model/configuration identifiers, schemas, aggregation, scoring, exclusions, and invalidation rules before execution. Record hashes and custody evidence.
- Persist and hash predictions and record missing outputs and deviations before reveal. A local hash detects changes; it does not by itself establish authenticity, independent chronology, or blindness.
- If forbidden information crosses the evaluation boundary, stop the affected confirmatory run, preserve an invalidation record, and notify the maintainer without reproducing the key. Deletion or instructions to ignore it do not restore blindness.
- Do not tune on the holdout, repair predictions after reveal, or discard unfavorable cases. A new evaluator version needs fresh confirmatory evidence.
- Treat a harness field such as `CONFIRMATORY` or `valid: true` as a software assertion requiring custody/protocol evidence, not automatic scientific validation.

## Privacy and publication

Follow `docs/experimental-standard/v0.1/PUBLICATION-SAFETY.md` and `SECURITY.md`.

- Use synthetic identifiers. Do not include secrets, private conversations, client traces, personal identifiers, private infrastructure paths, or unpublished answers in commits, logs, issues, PRs, or artifacts.
- Preserve scientifically relevant relationships during sanitization. If that cannot be done, stop publication of the affected artifact.
- Report a suspected credential exposure or deployed-system bypass privately through the documented disclosure route. Do not paste the sensitive value into a report.
- Automated scanning does not prove absence of secrets, semantic leaks, or identifying combinations. Review the proposed diff and artifacts manually too.
- Retain the repository's licensing split: code Apache-2.0; documentation, protocols, articles, taxonomies, diagrams, and public datasets CC BY 4.0. Do not change rights or add third-party material without a suitable basis.

## Offline fixture checks

The commands below are for the public integration fixture, from the repository root. They require Python 3 and Git, use no Python third-party dependencies, and write generated outputs to a fresh temporary directory. They are not a blind evaluation procedure. They read the already-public calibration labels; do not run them in an evaluator context reserved for unseen cases or when the current task prohibits label access.

```bash
set -eu
OUT="$(mktemp -d "${TMPDIR:-/tmp}/nirmata-review.XXXXXX")"
export PYTHONDONTWRITEBYTECODE=1
python3 --version
git rev-parse HEAD
git status --short
python3 reproducibility/scripts/validate.py
python3 reproducibility/scripts/baseline.py \
  --output "$OUT/predictions.jsonl" \
  --manifest "$OUT/manifest.json"
python3 reproducibility/scripts/score.py \
  --predictions "$OUT/predictions.jsonl" \
  --report "$OUT/score-report.json"
python3 -m unittest discover -s reproducibility/tests -v
python3 scripts/check_local_links.py
git diff --check
git status --short
printf 'Artifacts: %s\n' "$OUT"
```

Check each exit code. Stop on the first failed check and preserve its output; do not describe later, unexecuted checks as passed. Save logs and measure actual runtime and resource use when reporting a replication.

Current fixture validation expects 6 traces, 6 labels, and 1 applied trace. Confirm expectations against the pinned version. The baseline currently calls `validate_package`, which reads the public ground-truth file. Do not claim its execution is label-isolated or reuse it as a blind runner. The baseline manifest is not a complete file-access audit: record the public label file and other relevant inputs separately when reporting provenance.

## Additional gates

Read `.github/workflows/quality.yml` for the exact revision under review. On the reviewed `main`, CI uses Python 3.13, `jsonschema==4.25.1`, Experiment 002 schema/template validation, publication scanning, and Markdown lint in addition to the public fixture.

- `python3 scripts/validate_experiment_002.py` requires `jsonschema==4.25.1`. Use an isolated environment and record dependency versions; do not install silently into the user's global environment.
- `python3 scripts/audit_publication_safety.py --history` scans blobs reachable from local refs. Record checkout depth and available refs; a shallow or partial history is not a complete history audit.
- The contribution guide specifies `npx --yes markdownlint-cli2@0.23.2 "**/*.md" "#LICENSES/**"`. Installation needs network access. If unavailable or outside the approved scope, report that gate as not run.
- Verify `releases/v0.1.0/SHA256SUMS` only against the frozen tag/export, never current `main`. Do not regenerate archived hashes to make a changed tree pass.
- Add targeted regression tests for any changed behavior, then rerun affected checks. Report pass, fail, and not run separately. Never claim full CI success from a subset of local checks.

## Costs, limits, and completion

- Public review execution defaults to local/offline work: no paid APIs, model downloads, GPU jobs, new cloud resources, private datasets, or live external actions. Read-only code acquisition and authorized publication are separate steps. Dependency preparation may need network access. Do not promise a zero total cost: distinguish no paid inference from existing machine, connectivity, and service costs.
- Before any broader run, obtain approval for provider, data destination, model/checkpoint, maximum calls/tokens, spending cap, runtime, storage, and abort conditions. An estimate is not an enforced cap; report which limits the environment can actually enforce.
- Stop on unexpected network use, credential requests, data exposure, unexplained file mutation, resource limit, schema mismatch, or changed scope. Report the specific blocker and preserve safe evidence.
- Deliver: target commit; question; evidence class; inputs and hashes; environment; exact commands; exit codes; actual outputs; logs; elapsed time/cost if measured; deviations; limitations; and proposed next step. Include a diff for code changes.
- Use draft PRs when a PR is authorized, unless the maintainer asks otherwise. Publishing, merging, deploying, changing access, or starting a live holdout are separate actions. A review task does not authorize them.
