class Polygon:
    def get_data(self): pass
    def area(self): pass


class Rectangle(Polygon):
    def get_data(self):
        self.l = float(input("Enter length: "))
        self.w = float(input("Enter width: "))
    def area(self):
        return self.l * self.w

class Triangle(Polygon):
    def get_data(self):
        self.b = float(input("Enter base: "))
        self.h = float(input("Enter height: "))
    def area(self):
        return 0.5 * self.b * self.h

class Square(Polygon):
    def get_data(self):
        self.s = float(input("Enter side: "))
    def area(self):
        return self.s * self.s

# Main program
print("1.Rectangle 2.Triangle 3.Square")
choice = int(input("Choose shape: "))

if choice == 1:
    shape = Rectangle()
elif choice == 2:
    shape = Triangle()
elif choice == 3:
    shape = Square()
else:
    print("Invalid choice")
    exit()

shape.get_data()
print("Area =",shape.area())
