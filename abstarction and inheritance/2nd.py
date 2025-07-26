from abc import ABC, abstractmethod


# Abstract class (cannot be instantiated)
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method to be implemented in child classes

# child class inheriting from abstract class
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started. Vroom!")

    def stop_engine(self):
        print("Car engine stopped.")

# child class inheriting from abstract class
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started. Zoom!")

    def stop_engine(self):
        print("Bike engine stopped.")

# Demonstrating abstraction
carObj = Car()
carObj.start_engine()
carObj.stop_engine()

bikeObj = Bike()
bikeObj.start_engine()
