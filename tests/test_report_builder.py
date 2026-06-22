from report_builder import ReportBuilder, DragAndDropInterface, Report

def test_create_report():
    report_builder = ReportBuilder()
    drag_and_drop_interface = DragAndDropInterface(report_builder)
    report = drag_and_drop_interface.create_report("Test Report", "SELECT * FROM table", "2024-09-16 14:30:00")
    assert report.name == "Test Report"
    assert report.query == "SELECT * FROM table"
    assert report.schedule == "2024-09-16 14:30:00"

def test_schedule_report():
    report_builder = ReportBuilder()
    drag_and_drop_interface = DragAndDropInterface(report_builder)
    report = drag_and_drop_interface.create_report("Test Report", "SELECT * FROM table", "2024-09-16 14:30:00")
    drag_and_drop_interface.schedule_report(report)
    # Check that the report is scheduled
    assert report in report_builder.reports

def test_validate_report():
    report_builder = ReportBuilder()
    drag_and_drop_interface = DragAndDropInterface(report_builder)
    report = drag_and_drop_interface.create_report("Test Report", "SELECT * FROM table", "2024-09-16 14:30:00")
    assert drag_and_drop_interface.validate_report(report) == True

def test_validate_report_syntax_error():
    report_builder = ReportBuilder()
    drag_and_drop_interface = DragAndDropInterface(report_builder)
    report = drag_and_drop_interface.create_report("", "SELECT * FROM table", "2024-09-16 14:30:00")
    assert drag_and_drop_interface.validate_report(report) == False
