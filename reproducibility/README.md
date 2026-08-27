# Reproducibility package

**Language:** English · [Português (Brasil)](README.pt-BR.md)

**Status:** synthetic integration fixture, not a benchmark or confirmatory dataset.

This package makes Nirmata's factorized evaluation design executable with only the Python standard library. Six deliberately transparent calibration trajectories exercise benign behavior, unsafe content, a blocked unauthorized attempt, an executed policy violation, a harmful external effect, and a case where both evidence channels are unsafe.

## Run the package

```bash
python3 reproducibility/scripts/validate.py
python3 reproducibility/scripts/baseline.py \
  --output reproducibility/runs/example/predictions.jsonl
python3 reproducibility/scripts/score.py \
  --predictions reproducibility/runs/example/predictions.jsonl
python3 -m unittest discover -s reproducibility/tests -v
```

The baseline intentionally uses visible synthetic markers and simple rules. Its score verifies plumbing and expected distinctions only. It must not be reported as model performance, generalization, or confirmatory evidence.

## Package map

```text
schema/trajectory.schema.json       Versioned public trajectory schema
data/calibration/traces.jsonl       Six synthetic, labelled-by-design traces
data/calibration/ground_truth.jsonl Expected integration classifications
scripts/validate.py                 Structural and integrity validation
scripts/baseline.py                 Deterministic two-channel example evaluator
scripts/score.py                    Metrics and evidence-boundary report
tests/test_pipeline.py              End-to-end regression tests
runs/example/                       Generated example predictions and report
```

## Separation from future confirmation

The calibration labels are public and are loaded only by validation and scoring. The baseline reads traces but not the ground-truth file. Future blind holdouts must live outside this repository and outside the evaluator context until predictions have been persisted and hashed.

See the [methodology](../docs/METHODOLOGY.md), [evidence ledger](../docs/EVIDENCE-STATUS.md), and [research agenda](../docs/RESEARCH-AGENDA.md).
