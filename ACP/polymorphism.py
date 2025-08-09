import math

class Rectangle():
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Triangle():
    def _init_(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Circle():
    def _init_(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius**2)
