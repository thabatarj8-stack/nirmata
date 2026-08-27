from __future__ import annotations

import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from audit_publication_safety import scan_text  # noqa: E402


class PublicationSafetyTests(unittest.TestCase):
    def test_safe_research_text_passes(self) -> None:
        self.assertEqual(scan_text("safe.md", b"Synthetic trace ACTOR-01 has no private data."), [])

    def test_github_token_is_detected_without_exposing_value(self) -> None:
        content = b"ghp_" + (b"A" * 30)
        self.assertEqual(scan_text("fixture", content), ["fixture: GitHub token"])

    def test_email_is_detected(self) -> None:
        content = b"researcher" + b"@" + b"private.example"
        self.assertEqual(scan_text("fixture", content), ["fixture: email address"])

    def test_credential_bearing_url_is_detected(self) -> None:
        content = b"https://user:" + b"password" + b"@private.example/data"
        self.assertIn("fixture: credential-bearing URL", scan_text("fixture", content))


if __name__ == "__main__":
    unittest.main()
