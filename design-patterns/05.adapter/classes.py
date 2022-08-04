import json
import xmltodict

# Example 1
class DataProvider:
    """ An data provider object which always returns data in XML format """

    def get_xml_data(self):
        return """
            <employees>
                <employee>
                    <name>Jordan Raychev</name>
                    <role>Dev</role>
                </employee>
            </employees>
        """

class AdapterXMLToJson:
    """ XML to JSON adapter which acceepts a DataProvider objects and converts its
    data """

    def __init__(self, adaptee):
        self.data = adaptee.get_xml_data()

    def convert(self):
        return json.dumps(xmltodict.parse(self.data))


# Example 2
class Cat:   
    def meow(self):
        return "Cat meows"

class Dog:
    def bark(self):
        return "Dog barks"

class AnimalAdapter:
    """ An animal adapter """
    def __init__(self, obj, old_method, new_method):
        self.obj = obj
        self.__dict__[new_method] = old_method