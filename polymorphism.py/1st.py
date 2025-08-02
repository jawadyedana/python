class Person:
    def _init_(self, name, age, number):
        self.name = name
        self.age = age
        self.__number = number  # private attribute (double underscore)

    # getter 
    def get_details(self):
        print(f"hi my name is {self.name}, my age is {self.age} and my mobile phone number is {self.__number}")

    # setter 
    def set_number(self, newNumber):
        self.__number = newNumber
        print(f"hi {self.name}, your number has been updated to {self.__number}")

# creating objects
p1 = Person("izyan", 14, 998822)
p1.get_details()  # calling getter method
p1.set_number(899999)  # calling setter method
