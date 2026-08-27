# Contributing to Nirmata

Research critique, protocol review, replication attempts, and adversarial cases are welcome after the repository becomes public.

## Useful contributions

- identify a claim that is stronger than its evidence;
- review the blinding or ground-truth protocol;
- propose matched trajectory cases without exposing answers to evaluators;
- reproduce an evaluator on a different model or agentic system;
- improve the minimal trajectory schema;
- contribute an accessible article or substantive English/Portuguese translation that preserves evidence strength;
- report security or privacy risks privately.

## Evidence discipline

Contributions must label results as exploratory, development, integration, confirmatory, or invalidated. Do not convert calibration performance into a general claim, and do not remove failed runs from the record.

## Local checks

Run the public validation suite before opening a pull request:

```bash
python3 scripts/check_local_links.py
python3 reproducibility/scripts/validate.py
python3 -m unittest discover -s reproducibility/tests -v
npx --yes markdownlint-cli2@0.23.2 "**/*.md" "#LICENSES/**"
```

## Data safety

Do not submit secrets, private conversations, client data, access tokens, personal identifiers, or proprietary traces. Synthetic or explicitly consented traces are preferred.

## Contribution license

By contributing, you agree that software contributions are licensed under Apache-2.0 and documentation, article, protocol, taxonomy, diagram, and dataset contributions are licensed under CC BY 4.0.
