from abc import ABC, abstractmethod

class Color(ABC):
    
    @abstractmethod
    def paint(self):
        ...

class Vehicle(ABC):

    def __init__(self, color: Color):
        self.color = color
    
    @abstractmethod
    def apply_color(self):
        ...