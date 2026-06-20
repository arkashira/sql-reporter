from sql_reporter import SQLReporter, QueryResult

def test_execute_query():
    dataset = {
        'users': [
            {'id': '1', 'name': 'John', 'age': '30'},
            {'id': '2', 'name': 'Jane', 'age': '25'}
        ]
    }
    reporter = SQLReporter(dataset)
    query = 'SELECT * FROM users'
    result = reporter.execute_query(query)
    assert result.columns == ['id', 'name', 'age']
    assert result.rows == [['1', 'John', '30'], ['2', 'Jane', '25']]

def test_execute_query_invalid_table():
    dataset = {
        'users': [
            {'id': '1', 'name': 'John', 'age': '30'},
            {'id': '2', 'name': 'Jane', 'age': '25'}
        ]
    }
    reporter = SQLReporter(dataset)
    query = 'SELECT * FROM invalid_table'
    try:
        reporter.execute_query(query)
        assert False, 'Expected ValueError'
    except ValueError as e:
        assert str(e) == 'Table not found'

def test_format_result():
    result = QueryResult(['id', 'name', 'age'], [['1', 'John', '30'], ['2', 'Jane', '25']])
    reporter = SQLReporter({})
    formatted_result = reporter.format_result(result)
    assert formatted_result == 'id\tname\tage\n1\tJohn\t30\n2\tJane\t25\n'

def test_execute_query_invalid_query():
    dataset = {
        'users': [
            {'id': '1', 'name': 'John', 'age': '30'},
            {'id': '2', 'name': 'Jane', 'age': '25'}
        ]
    }
    reporter = SQLReporter(dataset)
    query = 'INVALID QUERY'
    try:
        reporter.execute_query(query)
        assert False, 'Expected ValueError'
    except ValueError as e:
        assert str(e) == 'Unsupported query'
