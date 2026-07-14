import json
from subprocess import run
import unittest

from src.text_checks import contains_keyword, has_min_words, quality_report, quality_score


class TextChecksTests(unittest.TestCase):
    def test_has_min_words(self) -> None:
        self.assertTrue(has_min_words("this sentence has at least eight words now", 8))
        self.assertFalse(has_min_words("too short", 3))

    def test_contains_keyword(self) -> None:
        self.assertTrue(contains_keyword("Django backend app", "django"))
        self.assertFalse(contains_keyword("Go service", "python"))

    def test_quality_score(self) -> None:
        score = quality_score("Project 2026 update includes tests and docs for release.")
        self.assertGreaterEqual(score, 50)

    def test_quality_report_flags(self) -> None:
        report = quality_report("ok")
        self.assertIn("too_short", report["flags"])

    def test_cli(self) -> None:
        result = run(
            [
                "python3",
                "cli.py",
                "Project 2026 update includes tests and docs for a polished release.",
                "--keyword",
                "tests",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertTrue(payload["keyword_found"])
        self.assertIn("score", payload)
        self.assertIn("flags", payload)


if __name__ == "__main__":
    unittest.main()
