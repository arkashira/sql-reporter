import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class DataWarehouse:
    name: str
    credentials: Dict[str, str]

class DataWarehouseManager:
    def __init__(self):
        self.warehouses = {}

    def add_warehouse(self, warehouse: DataWarehouse):
        self.warehouses[warehouse.name] = warehouse

    def get_warehouse(self, name: str) -> DataWarehouse:
        return self.warehouses.get(name)

    def test_connection(self, name: str) -> bool:
        # Simulate connection test
        return True

    def store_token(self, name: str, token: str):
        # Simulate token storage
        pass

    def get_connection_status(self, name: str) -> str:
        # Simulate connection status
        return "Connected"
