# Creating a tuple
fruits = ("apple", "banana", "cherry", "apple", "pineapple")

# Printing the tuple
print("Fruits tuple:", fruits)

# Accessing elements using index
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Accessing last element using negative index
print("Last fruit:", fruits[-1])

# Slicing a tuple
print("First two fruits:", fruits[0:2])

# Iterating over the tuple
for i in fruits:
    print(i)

# Counting occurrences
print("Apple count:", fruits.count("apple"))

# Finding index of an element
print("Index of banana:", fruits.index("banana"))
