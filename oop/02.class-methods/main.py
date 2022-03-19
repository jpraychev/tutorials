# main.py

def multiply(lstr: list[str]) -> int:
    lint = [int(el) for el in lstr]
    result = 1
    for el in lint:
        result *= el
    return result


class Material():
    attr = 'Common attribute between objects'

    def __init__(self, title, color, size):
        self.title = title
        self.color = color
        self.id = id(self)
        self.size = size
        
    def __repr__(self):
        return 'My Material class'
    
    def __str__(self):
        return 'My nicely formatted Material class'
    
    def pprint(self):
        print(f'Printing information for object {id(self)}')
        print(f'{self.title} has {self.color} color')

    @property
    def area(self):
        size = self.size.split('x')
        return f'Material area: {multiply(size)} square cm'
    
    @staticmethod
    def price(material):
        prices = {
            'wood' :'20 $',
            'glass' :'30 $',
            'steel' :'40 $'
        }
        return prices[material]
    
    @classmethod
    def from_dict(cls, obj_dict):
        vals = list(obj_dict.values())
        return cls(*vals)

d = {
    'title' : 'Wood',
    'color' : 'Brown',
    'size' : '80x150'
}

material = Material.from_dict(d)
print(material.title)
print(material.color)
print(material.size)