from classes import Color, Vehicle

class Red(Color):

    def paint(self):
        print(f'Painting using {__class__.__name__} color')

class Blue(Color):

    def paint(self):
        print(f'Painting using {__class__.__name__} color')

class Green(Color):

    def paint(self):
        print(f'Painting using {__class__.__name__} color')

class Car(Vehicle):

    def apply_color(self):
        self.color.paint()

class Bike(Vehicle):

    def apply_color(self):
        self.color.paint()

if __name__ == '__main__':   
    color = Blue()
    vw = Car(color)
    vw.apply_color()