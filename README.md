<h3 align="center">🛠️ sql-reporter</h3>

<div align="center">
  <a href="https://opensource.org/licenses/MIT" target="_blank">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
  </a>
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Language-Python-blue.svg" alt="Language: Python" />
  </a>
  <a href="https://github.com/axentx/sql-reporter/actions" target="_blank">
    <img src="https://img.shields.io/github/workflow/status/axentx/sql-reporter/Build" alt="Build Status" />
  </a>
  <a href="https://github.com/axentx/sql-reporter/stargazers" target="_blank">
    <img src="https://img.shields.io/github/stars/axentx/sql-reporter" alt="Stars" />
  </a>
</div>

---
# 🚀 sql-reporter
**Power developers and data engineers with automated SQL reporting.** Empower business users to generate reports and insights without relying on data engineers, reducing the workload on data engineers by automating routine reporting tasks.

## Why sql-reporter?
* **Easy to use**: User-friendly interface for non-technical users to run SQL queries and generate reports.
* **Automated reporting**: Automate routine reporting tasks, reducing the workload on data engineers.
* **Secure authentication**: Connects to cloud data warehouses using OAuth or key authentication, storing access tokens securely.
* **Flexible integration**: Supports multiple cloud data warehouses, including Snowflake, BigQuery, and Redshift.
* **Customizable**: Allows for customization of reporting dashboards to meet specific business needs.
* **Lightweight**: A small, efficient command-line application written in Python.
* **Scalable**: Designed to handle large datasets and high-volume reporting workloads.

## Feature Overview
| Feature | Description |
| --- | --- |
| Cloud Data Warehouse Support | Connects to Snowflake, BigQuery, and Redshift using OAuth or key authentication |
| Automated Reporting | Automates routine reporting tasks, reducing the workload on data engineers |
| Secure Token Storage | Stores access tokens securely using a vault |
| Customizable Reporting | Allows for customization of reporting dashboards to meet specific business needs |
| Lightweight CLI Application | A small, efficient command-line application written in Python |

## Tech Stack
* python
* poetry
* argparse

## Project Structure
* business: Business logic and requirements
* docs: Documentation and startup artifacts
* src: Source code for the sql-reporter application
* tests: Unit tests and integration tests for the application

## Getting Started
```bash
# Install dependencies using Poetry
poetry install

# Run the application
poetry run python src/main.py

# Run tests using Pytest
poetry run pytest tests
```

## Deploy
```bash
# Build and deploy the application using Poetry
poetry build
poetry publish
```

## Status
Last commit: d5a2ccc feat(sql-reporter): real, sandbox-tested implementation

## Contributing
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.