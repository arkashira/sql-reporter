import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class QueryResult:
    columns: List[str]
    rows: List[List[str]]

class SQLReporter:
    def __init__(self, dataset: Dict[str, List[Dict[str, str]]]):
        self.dataset = dataset

    def execute_query(self, query: str) -> QueryResult:
        # Simple query execution engine
        # Supports only SELECT * FROM table_name
        parts = query.split()
        if parts[0].upper() != 'SELECT' or parts[1] != '*' or parts[2].upper() != 'FROM':
            raise ValueError('Unsupported query')

        table_name = parts[3]
        if table_name not in self.dataset:
            raise ValueError('Table not found')

        columns = list(self.dataset[table_name][0].keys())
        rows = [[row[column] for column in columns] for row in self.dataset[table_name]]

        return QueryResult(columns, rows)

    def format_result(self, result: QueryResult) -> str:
        output = '\t'.join(result.columns) + '\n'
        for row in result.rows:
            output += '\t'.join(row) + '\n'
        return output

def main():
    dataset = {
        'users': [
            {'id': '1', 'name': 'John', 'age': '30'},
            {'id': '2', 'name': 'Jane', 'age': '25'}
        ]
    }
    reporter = SQLReporter(dataset)
    query = 'SELECT * FROM users'
    result = reporter.execute_query(query)
    print(reporter.format_result(result))

if __name__ == '__main__':
    main()
