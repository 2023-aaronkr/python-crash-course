# Dog.py
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} barks!")

    def sit(self):
        print(f"{self.name} sits!")

    def roll_over(self):
        print(f"{self.name} rolls over!")
