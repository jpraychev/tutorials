class Singleton:

    __instance = None
    
    def __new__(cls, *args, **kwargs):
        print(cls.__instance)
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

singleton = Singleton()
singleton.name = 'My first instance of Singleton class'
singleton1 = Singleton()
print(singleton.name)
print(singleton1.name)