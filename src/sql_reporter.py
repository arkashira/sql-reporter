import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Ticket:
    id: int
    closed_at: str

class SQLReporter:
    def __init__(self, tickets: List[Ticket]):
        self.tickets = tickets

    def get_closed_tickets_per_month(self):
        closed_tickets = {}
        for ticket in self.tickets:
            month = datetime.strptime(ticket.closed_at, '%Y-%m-%d').strftime('%Y-%m')
            if month not in closed_tickets:
                closed_tickets[month] = 0
            closed_tickets[month] += 1
        return closed_tickets

    def get_percentage_of_total_tickets(self, closed_tickets_per_month):
        total_tickets = len(self.tickets)
        percentages = {}
        for month, count in closed_tickets_per_month.items():
            percentages[month] = round((count / total_tickets) * 100, 2)
        return percentages

    def export_to_csv(self, closed_tickets_per_month, percentages):
        csv_data = 'Month,Closed Tickets,Percentage\n'
        for month, count in closed_tickets_per_month.items():
            csv_data += f'{month},{count},{percentages[month]}\n'
        return csv_data

def refresh_data_from_webhook(webhook_data):
    tickets = []
    for ticket in webhook_data:
        tickets.append(Ticket(id=ticket['id'], closed_at=ticket['closed_at']))
    return tickets
