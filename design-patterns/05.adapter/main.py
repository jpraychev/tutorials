# Example 1
from classes import DataProvider, AdapterXMLToJson, AnimalAdapter

adapter = AdapterXMLToJson(adaptee = DataProvider())
print(adapter.convert())

# Example 2
from classes import Cat, Dog

objects = [Cat(), Dog()]

for obj in objects:
    if hasattr(obj, 'meow'):
        obj = AnimalAdapter(obj, obj.meow, 'make_sound')
    if hasattr(obj, 'bark'):
        obj = AnimalAdapter(obj, obj.bark, 'make_sound')
    print(obj.make_sound())