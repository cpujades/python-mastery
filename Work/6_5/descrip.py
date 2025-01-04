# descrip.py

# exercise 4_3


class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f"{self.name} is being accessed by __get__")

    def __set__(self, instance, value):
        print(f"{self.name} is being set to {value} by __set__")

    def __delete__(self, instance):
        print(f"{self.name} is being deleted by __delete__")
