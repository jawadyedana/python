# Parent class
class Animal:
    def make_sound(self):
        return "Some generic animal sound"

# child class 1
class Dog(Animal):
    def make_sound(self):  # Overriding Parent method
        return "Bark"

# child class 2
class Cat(Animal):
    def make_sound(self):  # Overriding Parent method
        return "Meow"

# Testing Polymorphism
# creating objects
dog = Dog()
print(dog.make_sound())
cat = Cat()
print(cat.make_sound())
