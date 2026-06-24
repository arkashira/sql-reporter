import pytest
from sql_reporter import (
    WarehouseConnection,
    ConnectionRegistry,
    SnowflakeExecutor,
)

@pytest.fixture
def registry() -> ConnectionRegistry:
    reg = ConnectionRegistry()
    reg.add(
        WarehouseConnection(
            name="dev",
            user="alice",
            account="dev_account",
            warehouse="WH1",
            database="DB1",
            schema="SCHEMA1",
        )
    )
    return reg

def test_execute_success(registry):
    executor = SnowflakeExecutor(registry)
    result = executor.execute(
        connection_name="dev",
        query="SELECT * FROM table",
        user="alice",
        query_version="v1",
    )
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {"COLUMN1": 1, "COLUMN2": "a"}

def test_execute_error(registry):
    executor = SnowflakeExecutor(registry)
    with pytest.raises(RuntimeError) as exc:
        executor.execute(
            connection_name="dev",
            query="ERROR IN QUERY",
            user="alice",
            query_version="v1",
        )
    assert "Warehouse error" in str(exc.value)

def test_missing_connection(registry):
    executor = SnowflakeExecutor(registry)
    with pytest.raises(KeyError):
        executor.execute(
            connection_name="prod",
            query="SELECT 1",
            user="alice",
            query_version="v1",
        )
