# Experiment #002 blinding harness

Executable enforcement of the blinding protocol in
[protocol-v1.0.md](../protocol/protocol-v1.0.md) and the freeze requirements in
[the holdout definition](../holdout/README.md).

The first #002 holdout was invalidated because ground truth entered the
evaluator context before predictions existed. That failure was procedural, so
the remedy here is structural: the ordering is enforced by artifacts and module
boundaries rather than by operator memory.

## Context separation

| Module | Context | May read the key |
|---|---|---|
| `blinding.py` | shared | not applicable |
| `preflight.py` | curator | yes |
| `holdout_run.py` | evaluator | no code path exists |
| `holdout_reveal.py` | curator | only after verifying the prediction seal |
| `hub.py` | curator | yes |

`holdout_run.py` is the only module that runs in the evaluator context. It reads
traces, refuses key-like paths and environment variables, and has no import that
reaches the answer key.

## Stages

```bash
python3 preflight.py \
  --traces ~/nirmata-h2/traces/traces.jsonl \
  --key ~/nirmata-h2-key/answers.jsonl \
  --run-id NIR-002-H2-RUN-1 \
  --seal ~/nirmata-h2/freeze-seal.json
```

```bash
python3 holdout_run.py \
  --traces ~/nirmata-h2/traces/traces.jsonl \
  --output-dir ~/nirmata-h2/run-1 \
  --run-id NIR-002-H2-RUN-1 \
  --dataset-id Nirmata-88/nirmata-002-h2-traces \
  --dataset-version <full-commit-sha>
```

```bash
python3 holdout_reveal.py \
  --run-dir ~/nirmata-h2/run-1 \
  --key ~/nirmata-h2-key/answers.jsonl
```

Holdout material must live outside this repository, with traces and key in
separate directories. Preflight refuses otherwise.

## Seals

Each stage emits a seal recording a SHA-256 for every artifact and the UTC time
it was written. `holdout_reveal.py` verifies the `prediction_freeze` seal before
opening the key and exits without reading it if verification fails.

The sealed `run-manifest.json` is never rewritten. Reveal-time facts go to
`run-manifest.final.json`, so the seal that proves the ordering stays verifiable
after the reveal.

## External custody

Local seals prove integrity. They cannot prove ordering to a third party, since
both the artifact and its hash are held by the same author. `hub.py` publishes
the artifacts to two separate private dataset repositories on the Hugging Face
Hub, where the commit that carries the predictions is timestamped independently
and precedes the commit that publishes the key.

`hub.py` is the only module here that needs a network, and it dry-runs by
default.

## Backends

`offline-deterministic` is a transparent rule-based evaluator for dry runs. It
records `run_type` as `development` and must never be reported as model
performance or confirmatory evidence.

`hf-open-weights` calls an open-weight model through Hugging Face Inference
Providers, records `run_type` as `confirmatory`, and sets
`exact_weights_available` to true. Open weights are chosen so the run stays
reproducible against a fixed checkpoint; a closed endpoint can change beneath a
published result. Override the model with `NIRMATA_EVAL_MODEL`.

Each evaluator receives only what its frozen prompt permits: the content channel
sees `trace_id` and `final_output`, the trajectory channel sees `trace_id` and
ordered events. Withholding the output from the trajectory channel is what keeps
the OR aggregation a measure of incremental signal rather than of a shared look
at the same evidence.

A reply that does not parse, breaks the output contract, or carries the wrong
`trace_id` is recorded in `evaluator-failures.jsonl` and raised as a material
protocol deviation in the manifest. Failed traces get no prediction, so scoring
refuses the run rather than reporting a partial result as complete.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

Every guard has a test asserting that it fails closed.

`is_semantic_leak` in `preflight.py` implements a lexical policy: label
vocabulary is rejected in curator-authored trajectory prose, while
`final_output` is exempt because that text is the object under judgement rather
than a description of it. The policy is blunt and will reject legitimate
wording. A rejection is a prompt to rewrite the case, never a prompt to loosen
`LABEL_VOCABULARY` after seeing which case failed.
