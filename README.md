# Sandbox Testing Repo (Upgraded)

This repository is now a useful Python CLI project for quick text quality checks.
It can be used to score content drafts and verify keyword presence.

## Features

- CLI text scoring for short quality checks
- Optional keyword match validation
- Reusable helper module (`src/text_checks.py`)
- Automated tests including CLI execution

## Usage

```bash
python3 cli.py "Project 2026 update includes tests and docs." --keyword tests
```

## Run Tests

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## License

MIT License. See `LICENSE`.