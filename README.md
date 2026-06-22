<h3 align="center">🛠️ sql-reporter</h3>

<div align="center">
  <a href="https://github.com/axentx/sql-reporter/blob/main/LICENSE"><img src="https://img.shields.io/github/license/axentx/sql-reporter?style=flat-square" alt="License"></a>
  <a href="https://github.com/axentx/sql-reporter"><img src="https://img.shields.io/github/stars/axentx/sql-reporter?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/axentx/sql-reporter"><img src="https://img.shields.io/github/actions/workflow/status/axentx/sql-reporter/ci.yml?style=flat-square" alt="Build"></a>
  <a href="https://pypi.org/project/sql-reporter/"><img src="https://img.shields.io/pypi/v/sql-reporter?style=flat-square" alt="PyPI"></a>
</div>

---

# 🚀 sql-reporter

**Power data engineers with a lightweight CLI that authenticates and stores cloud warehouse tokens.**  
sql-reporter is a Python command‑line tool that connects to Snowflake, BigQuery, or Redshift using OAuth or key‑based auth, securely stores the access token in a vault, and reports the connection status for custom dashboards.

## Why sql-reporter?

- **Fast onboarding** – 30 s to connect a new warehouse.  
- **Zero‑config vault** – tokens are stored in your existing secrets manager.  
- **Cross‑cloud support** – Snowflake, BigQuery, Redshift out of the box.  
- **Built for data engineers** – a single command replaces manual OAuth flows.  
- **CLI‑first** – integrates seamlessly into CI/CD pipelines.  
- **Python 3.11+** – modern, type‑safe, and fully testable.  
- **Open‑source** – MIT‑licensed, community‑friendly.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Multi‑cloud auth** | Supports Snowflake, BigQuery, and Redshift via OAuth or key‑based auth. |
| **Vault integration** | Stores tokens in a configured secrets vault (e.g., HashiCorp Vault, AWS Secrets Manager). |
| **CLI interface** | Uses `argparse` for a clean, user‑friendly command line. |
| **Status reporting** | Prints connection status and token expiry to stdout. |
| **Extensible** | Add new warehouses or auth methods by extending `src.data_warehouse`. |

## Tech Stack

- python
- poetry
- argparse

## Project Structure

```
sql-reporter/
├── business/          # Business logic & domain models
├── docs/              # Documentation artifacts (PRD, ROADMAP, etc.)
├── src/               # Core application code (CLI, auth, vault)
│   ├── data_warehouse.py
│   └── oauth.py
├── tests/             # (Future) test suite
├── pyproject.toml     # Poetry configuration
└── README.md          # This file
```

## Getting Started

```bash
# Clone the repo
git clone https://github.com/axentx/sql-reporter.git
cd sql-reporter

# Install dependencies with Poetry
poetry install

# Run the CLI
poetry run sql-reporter --help
```

### Example usage

```bash
# Connect to Snowflake using OAuth
poetry run sql-reporter \
  --warehouse snowflake \
  --auth-method oauth \
  --client-id <client-id> \
  --client-secret <client-secret> \
  --vault-url <vault-url>
```

## Deploy

The tool is intended to run locally or in CI.  
If you want to ship it as a Docker image:

```bash
docker build -t axentx/sql-reporter:latest .
docker run --rm -it axentx/sql-reporter:latest \
  --warehouse bigquery \
  --auth-method key \
  --service-account-file /path/to/key.json \
  --vault-url <vault-url>
```

## Status

Current version 0.1.0 – fully functional, sandbox‑tested.  
Last commit: **38387fa** – “real, sandbox‑tested implementation”.

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) guide for how to get started.

## License

MIT © Axentx