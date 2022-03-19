# In this article we will be going over the basic dunder methods.
# The methods that we will look at are:

class Employee:

    def __init__(self, name:str, position:str, salary:int):
        self.__iter_data = list(locals().items())[1:]
        self.name = name
        self.position = position
        self.salary = salary
        self.__index = 0

    def __str__(self):
        return f'{self.name}:{self.position}:{self.salary}'

    def __len__(self):
        return len(self.__iter_data)

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary
        
    def __iter__(self):
        return self

    def __next__(self):
        try:
            val = self.__iter_data[self.__index]
            self.__index += 1
            return val
        except IndexError:
            raise StopIteration
    
    def __contains__(self, item):
        if item in str(self):
            return True
        return False

    def __call__(self):
        print('Calling call() method on object')