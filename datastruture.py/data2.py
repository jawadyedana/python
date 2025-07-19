# Dictionaries in Python

student = {
    "name": "Gaurav",
    "age": 15,
    "grade": "10th"
}  # Creating a dictionary

print("Original dictionary:", student)
# Accessing a value
print("Name of the student:", student["name"])

# Adding a new key-value pair
student["school"] = "ABC High School"
print("After adding 'school':", student)

# Updating a value
student["age"] = 16
print("After updating 'age':", student)

# Removing a key-value pair
del student["grade"]
print("After deleting 'grade':", student)

# Iterating through the dictionary
