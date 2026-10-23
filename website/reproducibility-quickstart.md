---
description: Run the public Nirmata baseline. It is deterministic and synthetic, not a model score and not confirmatory evidence.
---

# Reproducibility quickstart

!!! evidence "Synthetic baseline"

    The baseline is **deterministic and synthetic**. It uses visible synthetic markers and simple rules. It checks plumbing and expected distinctions. It is not a model score, not a benchmark, and not confirmatory evidence. It does not detect CVEs or language bugs.

Run the commands below from a checkout of the repository. This website does not execute them. The package uses the Python 3 standard library only.

The status line in the [reproducibility package](reproducibility/README.md) is: synthetic integration fixture, not a benchmark or confirmatory dataset.

## Run

```bash
python3 reproducibility/scripts/validate.py
python3 reproducibility/scripts/baseline.py \
  --output reproducibility/runs/example/predictions.jsonl \
  --manifest reproducibility/runs/example/manifest.json
python3 reproducibility/scripts/score.py \
  --predictions reproducibility/runs/example/predictions.jsonl \
  --report reproducibility/runs/example/score-report.json
python3 -m unittest discover -s reproducibility/tests -v
```

`validate.py` exits 0 and prints `status: ok` with 6 calibration traces, 6 labels, and 1 applied trace.

The baseline manifest records `claim_boundary`: "Pipeline verification only; not model performance or confirmatory evidence."

The score report records `claim_boundary`: "Calibration fixture only; do not report as model performance or confirmatory evidence."

## What the six traces are for

Six deliberately transparent calibration trajectories exercise benign behavior, unsafe content, a blocked unauthorized attempt, an executed policy violation, a harmful external effect, and a case where both evidence channels are unsafe.

Calibration labels are public. They are loaded only by validation and scoring. The baseline reads traces but not the ground-truth file. Future blind holdouts must live outside this repository and outside the evaluator context until predictions have been persisted and hashed.

## Check the frozen v0.1.0 archive

To check the frozen `v0.1.0` archive hashes, export that tag and run the checksum file from inside it. On current `main`, the same check does not apply: files changed after the tag when the DOI was published.

```bash
mkdir -p /tmp/nirmata-v0.1.0
git archive v0.1.0 | tar -x -C /tmp/nirmata-v0.1.0
( cd /tmp/nirmata-v0.1.0 && shasum -a 256 -c releases/v0.1.0/SHA256SUMS )
```

Continuous integration also validates Experiment 002 JSON Schemas after installing `jsonschema==4.25.1`. That step is separate from the dependency-free package above.

## Canonical package

File map, separation from future confirmation, and the same commands: [reproducibility package](reproducibility/README.md). Method and limits: [methodology](docs/METHODOLOGY.md). What the records support: [evidence ledger](docs/EVIDENCE-STATUS.md).
