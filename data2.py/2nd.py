# Creating a set
fruits_set = {"apple", "banana", "cherry", "apple"}
print("Fruits in the set:", fruits_set)

# Adding an element
fruits_set.add("pineapple")
print("Fruits after adding:", fruits_set)

# Removing an element
fruits_set.remove("cherry")
print("Fruits after removing:", fruits_set)

# Working with numbers set
numbers = {1, 2, 3, 4, 5, 1, 2}
print("Numbers set:", numbers)

# Adding an element
numbers.add(6)
print("After adding 6:", numbers)

# Removing an element
numbers.remove(3)
print("After removing 3:", numbers)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (combine all, remove duplicates)
print("Union:", set1.union(set2))  # 12345

# Intersection (common elements)
print("Intersection:", set1.intersection(set2))  # 3

# Difference
print("Difference (set1 - set2):", set1.difference(set2)) # 1 2
   