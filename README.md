# Sandbox Testing Repo (Upgraded)

<!-- BrandCloud:readme-standard -->
[![Maintained](https://img.shields.io/badge/Maintained-yes-brightgreen.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Showcase](https://img.shields.io/badge/Portfolio-Showcase-blue.svg)](#)

_Part of the `sakib-maho` project showcase series with consistent documentation and quality standards._

This repository is now a useful Python CLI project for quick text quality checks.
It can be used to score content drafts and verify keyword presence.

## Features

- CLI text scoring for short quality checks
- Optional keyword match validation
- Reusable helper module (`src/text_checks.py`)
- Automated tests including CLI execution

## Quick Start

```bash
python3 cli.py "Project 2026 update includes tests and docs." --keyword tests
```

## Tests

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## License

MIT License. See `LICENSE`.
