# main.py

class Material():
    attr = 'Common attribute between objects'

    def __init__(self, title, color):
        self.title = title
        self.color = color
        self.id = id(self)
        
    def __repr__(self):
        return 'My Material class'
    
    def __str__(self):
        return 'My nicely formatted Material class'