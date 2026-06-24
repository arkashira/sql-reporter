import pytest
from sql_reporter import SQLReporter

def test_connect_to_data_warehouse():
    reporter = SQLReporter()
    result = reporter.connect_to_data_warehouse("Snowflake")
    assert result == {"connection": "snowflake://user:password@account"}

def test_connect_to_unsupported_data_warehouse():
    reporter = SQLReporter()
    with pytest.raises(ValueError):
        reporter.connect_to_data_warehouse("Unknown")

def test_execute_query():
    reporter = SQLReporter()
    result = reporter.execute_query("Snowflake", "SELECT * FROM table")
    assert len(result) == 10
    assert result[0] == "Result 0"

def test_get_data_warehouses():
    reporter = SQLReporter()
    result = reporter.get_data_warehouses()
    assert len(result) == 3
    assert "Snowflake" in result
    assert "BigQuery" in result
    assert "Redshift" in result
