# Add all relevant classes for prototype tutorial here and use them in your
# main.py file
# Article on medium: https://medium.com/p/f0f8facd8934/edit

import copy


class ProblemTicket:

    def __init__(
        self,
        name:str,
        description:str,
        labels:list[str],
        priority:str,
        reporter:str
    ) -> None:
        self.name = name
        self.description = description
        self.labels = labels
        self.priority = priority
        self.reporter = reporter


class Prototype:
    
    registry = {}

    @staticmethod
    def register(identifier, obj):
        __class__.registry[identifier] = obj

    @staticmethod
    def unregister(identifier):
        del __class__[identifier]

    @staticmethod
    def clone(identifier):
        try:
            obj = __class__.registry[identifier]
            return copy.deepcopy(obj)
        except KeyError:
            raise KeyError(f'Object not found in registry') from None
        except copy.Error:
            raise copy.Error(f'Not able to copy {obj}') from None