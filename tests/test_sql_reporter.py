import pytest
from sql_reporter import SQLReporter, Ticket, refresh_data_from_webhook

def test_get_closed_tickets_per_month():
    tickets = [
        Ticket(1, '2022-01-01'),
        Ticket(2, '2022-01-15'),
        Ticket(3, '2022-02-01'),
    ]
    reporter = SQLReporter(tickets)
    closed_tickets_per_month = reporter.get_closed_tickets_per_month()
    assert closed_tickets_per_month == {'2022-01': 2, '2022-02': 1}

def test_get_percentage_of_total_tickets():
    tickets = [
        Ticket(1, '2022-01-01'),
        Ticket(2, '2022-01-15'),
        Ticket(3, '2022-02-01'),
    ]
    reporter = SQLReporter(tickets)
    closed_tickets_per_month = reporter.get_closed_tickets_per_month()
    percentages = reporter.get_percentage_of_total_tickets(closed_tickets_per_month)
    assert percentages == {'2022-01': 66.67, '2022-02': 33.33}

def test_export_to_csv():
    tickets = [
        Ticket(1, '2022-01-01'),
        Ticket(2, '2022-01-15'),
        Ticket(3, '2022-02-01'),
    ]
    reporter = SQLReporter(tickets)
    closed_tickets_per_month = reporter.get_closed_tickets_per_month()
    percentages = reporter.get_percentage_of_total_tickets(closed_tickets_per_month)
    csv_data = reporter.export_to_csv(closed_tickets_per_month, percentages)
    assert csv_data == 'Month,Closed Tickets,Percentage\n2022-01,2,66.67\n2022-02,1,33.33\n'

def test_refresh_data_from_webhook():
    webhook_data = [
        {'id': 1, 'closed_at': '2022-01-01'},
        {'id': 2, 'closed_at': '2022-01-15'},
        {'id': 3, 'closed_at': '2022-02-01'},
    ]
    tickets = refresh_data_from_webhook(webhook_data)
    assert len(tickets) == 3
    assert tickets[0].id == 1
    assert tickets[0].closed_at == '2022-01-01'
