import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Report:
    name: str
    query: str
    schedule: str

class ReportBuilder:
    def __init__(self):
        self.reports = []

    def create_report(self, name: str, query: str, schedule: str) -> Report:
        report = Report(name, query, schedule)
        self.reports.append(report)
        return report

    def schedule_report(self, report: Report) -> None:
        # Simulate scheduling the report
        print(f"Scheduling report {report.name} to run at {report.schedule}")

    def validate_report(self, report: Report) -> bool:
        # Simulate validating the report for syntax errors
        try:
            # Check for basic syntax errors
            if not report.name or not report.query or not report.schedule:
                return False
            return True
        except Exception as e:
            print(f"Error validating report: {e}")
            return False

class DragAndDropInterface:
    def __init__(self, report_builder: ReportBuilder):
        self.report_builder = report_builder

    def create_report(self, name: str, query: str, schedule: str) -> Report:
        return self.report_builder.create_report(name, query, schedule)

    def schedule_report(self, report: Report) -> None:
        self.report_builder.schedule_report(report)

    def validate_report(self, report: Report) -> bool:
        return self.report_builder.validate_report(report)
