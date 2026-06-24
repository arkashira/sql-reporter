import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class DataWarehouse:
    name: str
    connection_string: str

class SQLReporter:
    def __init__(self):
        self.data_warehouses = {
            "Snowflake": DataWarehouse("Snowflake", "snowflake://user:password@account"),
            "BigQuery": DataWarehouse("BigQuery", "bigquery://project-id"),
            "Redshift": DataWarehouse("Redshift", "redshift://user:password@host:port/dbname")
        }

    def connect_to_data_warehouse(self, data_warehouse_name: str) -> Dict:
        if data_warehouse_name in self.data_warehouses:
            return {"connection": self.data_warehouses[data_warehouse_name].connection_string}
        else:
            raise ValueError("Unsupported data warehouse")

    def execute_query(self, data_warehouse_name: str, query: str) -> List:
        # Simulate query execution
        return [f"Result {i}" for i in range(10)]

    def get_data_warehouses(self) -> List:
        return list(self.data_warehouses.keys())
