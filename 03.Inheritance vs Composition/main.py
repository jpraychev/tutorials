class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return self.name
        
    def give_treat(self) -> str:
        print(f'{self} received a treat!')

class HomePet(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

class Dog(HomePet):
    
    def give_treat(self) -> str:
        return f'{self.name} received a treat from {__class__.__name__} class'

class DogComposition(HomePet):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.tail = Tail('short')
    
    def tail_info(self):
        return f'{self.name} has a {self.tail.length} tail'

class Cat(HomePet):
    pass

class Tail:
    def __init__(self, length):
        self.length = length


if __name__ == '__main__':
    dog = Dog('Charley', 5, 'Drathard')
    cat = Cat('Thomas', 7, 'Persian')
    print(dog.give_treat())
    cat.give_treat()
    dog_comp = DogComposition('Charley', 5, 'Drathard')
    print(dog_comp.tail_info())
