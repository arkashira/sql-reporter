import pytest
from src.data_warehouse import DataWarehouse, DataWarehouseManager

def test_add_warehouse():
    manager = DataWarehouseManager()
    warehouse = DataWarehouse("Snowflake", {"username": "user", "password": "password"})
    manager.add_warehouse(warehouse)
    assert manager.get_warehouse("Snowflake") == warehouse

def test_test_connection():
    manager = DataWarehouseManager()
    warehouse = DataWarehouse("Snowflake", {"username": "user", "password": "password"})
    manager.add_warehouse(warehouse)
    assert manager.test_connection("Snowflake") == True

def test_store_token():
    manager = DataWarehouseManager()
    warehouse = DataWarehouse("Snowflake", {"username": "user", "password": "password"})
    manager.add_warehouse(warehouse)
    manager.store_token("Snowflake", "token")
    # Simulate token storage

def test_get_connection_status():
    manager = DataWarehouseManager()
    warehouse = DataWarehouse("Snowflake", {"username": "user", "password": "password"})
    manager.add_warehouse(warehouse)
    assert manager.get_connection_status("Snowflake") == "Connected"
