<h3 align="center">🛠️ sql-reporter</h3>

<div align="center">
  <a href="https://opensource.org/licenses/MIT" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://github.com/axentx/sql-reporter" target="_blank">
    <img alt="GitHub repository" src="https://img.shields.io/badge/repository-axentx/sql--reporter-blue" />
  </a>
  <a href="https://github.com/axentx/sql-reporter/actions" target="_blank">
    <img alt="Build status" src="https://img.shields.io/github/actions/workflow/status/axentx/sql-reporter/build.yml?branch=main" />
  </a>
  <a href="https://github.com/axentx/sql-reporter/stargazers" target="_blank">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/axentx/sql-reporter?style=social" />
  </a>
</div>

---
# 🚀 sql-reporter
**Power data analysts with automated SQL report creation and scheduling for data warehouses.** SQL Reporter is a Python-based application that allows users to create and manage SQL reports from various data warehouses, making it easier to manage data warehouse reports.

## Why sql-reporter?
* **Automated reporting**: Automate SQL report creation and scheduling for data warehouses.
* **OAuth authentication**: Secure authentication with OAuth for data warehouses.
* **Command-line interface**: Easy-to-use command-line interface for creating new reports.
* **Data warehouse support**: Interacts with various data warehouses to retrieve connection status.
* **Token storage**: Stores authentication tokens for secure report creation.
* **Scheduling**: Schedule reports to run at specific intervals.
* **Customizable**: Allows users to customize report creation and scheduling.

## Feature Overview
| Feature | Description |
| --- | --- |
| Automated reporting | Automate SQL report creation and scheduling |
| OAuth authentication | Secure authentication with OAuth for data warehouses |
| Command-line interface | Easy-to-use command-line interface for creating new reports |
| Data warehouse support | Interacts with various data warehouses to retrieve connection status |
| Token storage | Stores authentication tokens for secure report creation |
| Scheduling | Schedule reports to run at specific intervals |

## Tech Stack
* Python
* Poetry
* Pytest
* OAuth

## Project Structure
* `business`: Business logic and models
* `docs`: Documentation and guides
* `src`: Source code for the application
* `tests`: Unit tests and integration tests

## Getting Started
```bash
# Install dependencies
poetry install

# Run the application
poetry run python src/main.py

# Run tests
poetry run pytest tests
```

## Deploy
```bash
# Build the application
poetry build

# Deploy to production
# TODO: Add deployment script
```

## Status
Last commit: `46dccae` - feat(sql-reporter): real, sandbox-tested implementation

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for more information on contributing to sql-reporter.

## License
Licensed under the MIT License. See [LICENSE](LICENSE) for more information.