from abc import ABC, abstractmethod

class Ticket(ABC):
    @abstractmethod
    def ticket_type():
        pass

class IncidentTicket(Ticket):
    def ticket_type():
        return f'{__class__.__name__} has been created'

class ProblemTicket(Ticket):
    def ticket_type():
        return f'{__class__.__name__} has been created'

class ServiceRequest(Ticket):
    def ticket_type():
        return f'{__class__.__name__} has been created'

class TicketFactory:
    @staticmethod
    def create_ticket(t_type):

        tickets = {
                'incident' : IncidentTicket,
                'problem': ProblemTicket,
                'servicerequest' : ServiceRequest
        }

        assert t_type in tickets, f'Ticket type "{t_type}" is not supported'
        return tickets[t_type]

def client_code(ticket_type):
    factory = TicketFactory()
    ticket = factory.create_ticket(ticket_type)
    print(ticket.ticket_type())

if __name__ == '__main__':
    client_code('incident')
    client_code('problem')
    client_code('servicerequest')