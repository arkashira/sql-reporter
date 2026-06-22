# SQL Reporter

This project provides a data warehouse integration layer for SQL reporting.

## Features

* Supports OAuth and key-based authentication for Snowflake, BigQuery, and Redshift
* Connection tests succeed and store a secure token in the vault
* Connection status is displayed in the dashboard

## Usage

1. Install the project using `poetry install`
2. Run the project using `python src/main.py --warehouse <warehouse_name> --credentials <credentials>`
