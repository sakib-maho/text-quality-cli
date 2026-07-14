# Text Quality CLI

Python CLI that scores short-form text and returns actionable writing flags.

## Features

- Word/sentence stats
- Approximate readability score
- Duplicate-word and passive-voice heuristics
- Optional keyword presence check
- JSON report output for tooling/pipelines
- Unit + CLI tests

## Quick start

```bash
python3 cli.py "Project 2026 update includes tests and docs for release." --keyword tests
python3 -m unittest discover -s tests -p "test_*.py"
```

## Example output

```json
{
  "word_count": 10,
  "score": 85,
  "flags": [],
  "keyword_found": true
}
```

## License

MIT
