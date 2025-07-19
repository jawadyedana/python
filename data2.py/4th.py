# Initialize a set with duplicate values
my_set = {1, 2, 2, 3, 4, 4, 4}
print("Set:", my_set)

# Add an element to the set
my_set.add(5)
print("Updated Set:", my_set)

# Define two sets
set1 = my_set #(1,2,3,4,5)
set2 = {2, 4, 4, 6}

# Print sets and their differences
print("\nSet 1:", set1)
print("Set 2:", set2)
print("Difference:")
print(set1.difference(set2))
print("Symmetric Difference:")
print(set1.symmetric_difference(set2))