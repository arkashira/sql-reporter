import json
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Tuple


@dataclass
class WarehouseConnection:
    name: str
    user: str
    account: str
    warehouse: str
    database: str
    schema: str


class ConnectionRegistry:
    """
    Holds configured warehouse connections.
    """
    def __init__(self) -> None:
        self._connections: Dict[str, WarehouseConnection] = {}

    def add(self, conn: WarehouseConnection) -> None:
        self._connections[conn.name] = conn

    def get(self, name: str) -> WarehouseConnection:
        if name not in self._connections:
            raise KeyError(f"Connection '{name}' not found")
        return self._connections[name]

    def list(self) -> List[str]:
        return list(self._connections.keys())


class MockSnowflakeCursor:
    """
    Simulates a Snowflake cursor. Returns dummy data.
    """
    def __init__(self, query: str) -> None:
        self.query = query
        self.description = [("COLUMN1",), ("COLUMN2",)]
        self._rows = [(1, "a"), (2, "b")]

    def execute(self, query: str) -> None:
        if "ERROR" in query.upper():
            raise RuntimeError("Simulated warehouse error")
        # Simulate execution time
        time.sleep(0.1)

    def fetchall(self) -> List[Tuple[Any, ...]]:
        return self._rows

    def close(self) -> None:
        pass


class MockSnowflakeConnection:
    """
    Simulates a Snowflake connection.
    """
    def __init__(self, conn: WarehouseConnection) -> None:
        self.conn = conn

    def cursor(self) -> MockSnowflakeCursor:
        return MockSnowflakeCursor("")

    def close(self) -> None:
        pass


class SnowflakeExecutor:
    """
    Executes SQL against a configured Snowflake connection.
    """
    def __init__(self, registry: ConnectionRegistry) -> None:
        self.registry = registry

    def _log(self, user: str, query: str, version: str) -> None:
        log_entry = {
            "user": user,
            "query_version": version,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "query": query,
        }
        # For this example we just print the log. In real life, write to file or DB.
        print(json.dumps(log_entry))

    def execute(
        self,
        connection_name: str,
        query: str,
        user: str,
        query_version: str,
    ) -> List[Dict[str, Any]]:
        """
        Execute the given query on the specified warehouse connection.
        Returns list of row dicts.
        Raises RuntimeError if warehouse returns an error.
        """
        conn_cfg = self.registry.get(connection_name)
        self._log(user, query, query_version)

        # Simulate connection
        conn = MockSnowflakeConnection(conn_cfg)
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            # Convert to list of dicts
            result = [dict(zip([col[0] for col in cursor.description], row)) for row in rows]
            return result
        except Exception as e:
            raise RuntimeError(f"Warehouse error: {e}") from e
        finally:
            cursor.close()
            conn.close()
