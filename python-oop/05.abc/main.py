from abc import ABC, abstractmethod

class Ticket(ABC):

    @abstractmethod
    def title(self):
        pass

    @abstractmethod
    def priority(self):
        pass

    @abstractmethod
    def description(self):
        pass


class IncidentTicket(Ticket):

    def __init__(self):
        self.start_time = self.__start_time()

    def title(self):
        return 'Ticket title'

    def priority(self):
        return 'Ticket priority'

    def description(self):
        return 'Ticket description'

    def __start_time(self):
        from datetime import datetime
        return datetime.now()