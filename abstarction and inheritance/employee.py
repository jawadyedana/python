# parent class
class Person(object):
    # _init_ is known as the constructor
    def _init_(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee(Person):
    def _init_(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the _init_ of the parent class
        Person._init_(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Penguin', 20210401, 15000, "Intern")

# calling a function of the class Person using its instance
a.display()
