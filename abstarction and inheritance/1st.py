from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract method (details hidden)

# Child Class 1
class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} Bark")

    def walk(self):
        print(f"{self.name} is walking")

# Child Class 2
class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} Meow")

    def walk(self):
        print(f"{self.name} is walking")

# Main Code
dog = Dog("Scooby")
cat = Cat("Tio")
dog.walk()
dog.sound()
cat.walk()
cat.sound()
