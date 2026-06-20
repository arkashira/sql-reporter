<h3 align="center">🛠️ sql-reporter</h3>

<div align="center">
  <a href="https://github.com/your-org/sql-reporter"><img src="https://img.shields.io/github/license/your-org/sql-reporter?color=blue" alt="License"></a>
  <a href="https://github.com/your-org/sql-reporter"><img src="https://img.shields.io/github/languages/top/your-org/sql-reporter?color=orange" alt="Language"></a>
  <a href="https://github.com/your-org/sql-reporter/actions"><img src="https://img.shields.io/github/actions/workflow/status/your-org/sql-reporter/ci.yml?branch=main&label=build" alt="Build"></a>
  <a href="https://github.com/your-org/sql-reporter/stargazers"><img src="https://img.shields.io/github/stars/your-org/sql-reporter?style=social" alt="Stars"></a>
</div>

---

# 🚀 sql-reporter
**Power data engineers with instant, reproducible SQL execution reports.**  
Generate clean, version‑controlled reports from any SQL script, complete with execution metrics, result snapshots, and CI‑ready artifacts.

## Why sql-reporter?
- **Zero‑setup reporting** – Run a single command and get a full HTML/Markdown report, no manual copy‑pasting.
- **Built for CI/CD pipelines** – Emits machine‑readable JSON alongside human‑friendly docs, perfect for GitHub Actions or GitLab CI.
- **Execution transparency** – Captures query duration, rows returned, and execution plan for every statement.
- **Version‑controlled artifacts** – Reports are stored alongside your code, enabling audit trails and rollback checks.
- **Database‑agnostic** – Works with PostgreSQL, MySQL, SQLite, and any DBAPI‑compatible driver.
- **Extensible plugins** – Hook into custom post‑processing or alerting via a simple Python plugin system.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **One‑click report generation** | `sql-reporter run path/to/query.sql` produces HTML, Markdown, and JSON outputs. |
| **Multi‑dialect support** | Auto‑detects PostgreSQL, MySQL, SQLite, or uses explicit `--dialect` flag. |
| **Execution metrics** | Logs duration, rows, and EXPLAIN plan for each statement. |
| **CI integration** | Exit codes reflect success/failure; artifacts can be uploaded as CI artifacts. |
| **Custom plugins** | Drop a Python module in `plugins/` to add post‑run actions (e.g., Slack alerts). |
| **Configurable via TOML** | Global defaults live in `pyproject.toml` under `[tool.sql-reporter]`. |

## Tech Stack
*The tech‑stack decisions are defined in `decisions/tech-stack.md`. No additional technologies have been introduced beyond those locked in that file.*

## Project Structure
```
sql-reporter/
├─ business/          # Domain‑level logic (report generation, metrics aggregation)
├─ docs/              # Documentation assets (README, PRD, etc.)
├─ src/               # Core library code (SQL execution, parsers, plugins)
├─ tests/             # Unit and integration test suite
├─ pyproject.toml     # Build system, dependencies, entry points
└─ README.md          # This file
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/your-org/sql-reporter.git
cd sql-reporter

# Install the package in editable mode (uses the build system defined in pyproject.toml)
pip install -e .

# Verify the installation
sql-reporter --help
```

### Running a Report

```bash
# Generate a report for a SQL file
sql-reporter run examples/sample_query.sql

# Output files (by default) are placed in ./reports/
# - report.html
# - report.md
# - report.json
```

### Running Tests

```bash
# Execute the full test suite
pytest -q
```

## Deploy

The project is a pure Python library; deployment consists of publishing to PyPI.

```bash
# Build the distribution packages
python -m build

# Upload to PyPI (requires proper credentials)
twine upload dist/*
```

## Status
🚧 **Active development** – latest commit `dbca86b` adds a sandbox‑tested implementation of the core reporter.

## Contributing
We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to submit issues, feature requests, and pull requests.

## License
This project is licensed under the **MIT License**.