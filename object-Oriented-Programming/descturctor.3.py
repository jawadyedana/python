class Person:
    # Constructor to initialize name and age
    def _init_(self, name, age):
        self.name = name
        self.age = age
        print(f"Hello, {self.name}! Your age is {self.age}. Object has been created!")

    # Method to display a greeting
    def greet(self):
        print(f"Welcome, {self.name}! Have a great day!")

    # Destructor to clean up
    def _del_(self):
        print(f"Goodbye, {self.name}! Your data is being deleted.")

# Creating an object of the Person class
print("Creating a Person object...")
person1 = Person("Sadia", 25)  # Constructor is called here

# Using the greet method
print("Calling the greet method...")
person1.greet()

# Deleting the object
print("Deleting the Person object...")
del person1  # Destructor is called here
