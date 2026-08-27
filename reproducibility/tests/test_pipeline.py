from __future__ import annotations

import sys
import tempfile
import unittest
import copy
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from baseline import run  # noqa: E402
from score import score  # noqa: E402
from common import load_jsonl  # noqa: E402
from validate import validate_package, validate_trace  # noqa: E402


class ReproducibilityPipelineTests(unittest.TestCase):
    def test_calibration_package_is_valid(self) -> None:
        self.assertEqual(validate_package(), {"traces": 6, "labels": 6})

    def test_end_to_end_fixture_preserves_expected_distinctions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            predictions_path = root / "predictions.jsonl"
            manifest_path = root / "manifest.json"
            predictions = run(predictions_path, manifest_path)
            report = score(predictions_path)

        self.assertEqual(len(predictions), 6)
        self.assertEqual(report["content_accuracy"], 1.0)
        self.assertEqual(report["trajectory_class_accuracy"], 1.0)
        self.assertEqual(report["trajectory_aware_accuracy"], 1.0)
        self.assertEqual(report["incremental_true_detections"], 2)
        self.assertGreater(report["unsafe_acceptance_rate_final_only"], 0.0)

    def test_modified_content_fails_hash_validation(self) -> None:
        trace = copy.deepcopy(load_jsonl(Path(__file__).resolve().parents[1] / "data" / "calibration" / "traces.jsonl")[0])
        trace["final_output"]["content"] = "Modified after approval"
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            validate_trace(trace)

    def test_unknown_event_field_is_rejected(self) -> None:
        trace = copy.deepcopy(load_jsonl(Path(__file__).resolve().parents[1] / "data" / "calibration" / "traces.jsonl")[0])
        trace["events"][0]["untracked"] = True
        with self.assertRaisesRegex(ValueError, "unexpected keys"):
            validate_trace(trace)


if __name__ == "__main__":
    unittest.main()
