class Student:
    def _init_(self, name, age, grade):
        if not isinstance(name, str) or not isinstance(age, int) or not isinstance(grade, str):
            raise ValueError("Invalid data type for student attributes")
        self.name = name
        self.age = age
        self.grade = grade
        print(f"\nStudent record created for {self.name}.")

    def _str_(self):
        return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}"

    def updateGrade(self, new_grade):
        if not isinstance(new_grade, str):
            raise ValueError("Invalid data type for grade")
        self.grade = new_grade
        print(f"{self.name}'s grade has been updated to {self.grade}.")

    def _del_(self):
        print(f"Student record for {self.name} has been deleted.")

# Create student objects
try:
    student1 = Student("Anjali", 14, "8th")
    print(student1)
    student1.updateGrade("9th")

    student2 = Student("Rahul", 15, "9th")
    print(student2)

# Delete student2 object
    del student2  # Destructor will be called here
except ValueError as e:
 print(e)
