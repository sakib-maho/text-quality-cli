"""CLI for running lightweight text quality checks."""

from __future__ import annotations

import argparse
import json

from src.text_checks import contains_keyword, quality_score


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sandbox-check",
        description="Run quick quality checks for text snippets.",
    )
    parser.add_argument("text", help="Text to evaluate")
    parser.add_argument("--keyword", default="", help="Optional keyword to match")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    payload = {
        "score": quality_score(args.text),
        "keyword_match": contains_keyword(args.text, args.keyword) if args.keyword else None,
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
