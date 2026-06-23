from sql_reporter import SQLReporter, Report

def test_create_report():
    reporter = SQLReporter()
    report = reporter.create_report("Test Report", "SELECT * FROM test_table", "daily")
    assert report.id == 1
    assert report.name == "Test Report"
    assert report.query == "SELECT * FROM test_table"
    assert report.schedule == "daily"

def test_schedule_report():
    reporter = SQLReporter()
    report = reporter.create_report("Test Report", "SELECT * FROM test_table", "daily")
    scheduled_report = reporter.schedule_report(report.id, "weekly")
    assert scheduled_report.id == report.id
    assert scheduled_report.name == report.name
    assert scheduled_report.query == report.query
    assert scheduled_report.schedule == "weekly"

def test_execute_report():
    reporter = SQLReporter()
    report = reporter.create_report("Test Report", "SELECT * FROM test_table", "daily")
    result = reporter.execute_report(report.id)
    assert result["report_id"] == report.id
    assert result["query"] == report.query
    assert result["result"] == "Report executed successfully"

def test_optimize_report_execution():
    reporter = SQLReporter()
    report = reporter.create_report("Test Report", "SELECT * FROM test_table", "daily")
    result = reporter.optimize_report_execution(report.id)
    assert result["report_id"] == report.id
    assert result["query"] == report.query
    assert result["result"] == "Report execution optimized"

def test_report_not_found():
    reporter = SQLReporter()
    try:
        reporter.execute_report(1)
        assert False
    except ValueError as e:
        assert str(e) == "Report not found"
