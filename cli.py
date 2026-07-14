"""CLI for running lightweight text quality checks."""

from __future__ import annotations

import argparse
import json

from src.text_checks import quality_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="text-quality-cli",
        description="Score text quality and surface writing flags.",
    )
    parser.add_argument("text", help="Text to evaluate")
    parser.add_argument("--keyword", default="", help="Optional keyword that should appear")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report = quality_report(args.text, keyword=args.keyword or None)
    print(json.dumps(report, indent=2))
    return 0 if report["score"] >= 50 else 1


if __name__ == "__main__":
    raise SystemExit(main())
