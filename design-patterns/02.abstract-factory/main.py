# Abstract Factory
from abc import ABC, abstractmethod

class Ticket(ABC):

    @abstractmethod
    def info(self): pass

class IncidentTicket(Ticket):

    def info(self):
        return self.__class__.__name__

class ProblemTicket(Ticket):

    def info(self):
        return self.__class__.__name__

class AbstractFactory(ABC):

    @abstractmethod
    def create_ticket(self, type):
        pass

class JiraFactory(AbstractFactory):

    def create_ticket(self, type):
        if type == 'incident': return IncidentTicket()
        if type == 'problem': return ProblemTicket()

class SnowFactory(AbstractFactory):

    def create_ticket(self, type):
        if type == 'incident': return IncidentTicket()

class FactoryProducer:

    def get_factory(self, type):
        if type == 'jira': return JiraFactory()
        if type == 'snow': return SnowFactory()
        
if __name__ == '__main__':

    producer = FactoryProducer()
    jira_factory = producer.get_factory('jira')
    snow_factory = producer.get_factory('snow')
    jira_incident = jira_factory.create_ticket('incident')
    jira_problem = jira_factory.create_ticket('problem')
    snow_incident = snow_factory.create_ticket('incident')
    print(jira_incident)
    print(jira_problem)
    print(snow_incident)
    print(jira_incident.info())
    print(jira_problem.info())
    print(snow_incident.info())