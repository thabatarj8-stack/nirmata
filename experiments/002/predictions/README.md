# Prediction artifacts

The `*.template.jsonl` files in this directory are **shape examples only**. Their placeholder values are not experimental predictions and must never be scored or cited as results.

For a real run:

1. write outputs to new run-specific files, for example `content-predictions.RUN-001.jsonl` and `trajectory-predictions.RUN-001.jsonl`;
2. validate each line against `../schemas/prediction.schema.json`;
3. persist and hash the completed prediction artifacts before ground-truth reveal;
4. record those hashes in the run manifest and freeze record;
5. do not overwrite or manually repair confirmatory predictions after reveal.

Templates use synthetic identifiers only and contain no ground truth.