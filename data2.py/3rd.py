# Creating an empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# Tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# Nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# Accessing tuple elements using indexing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])  # First element
# print(my_tuple[5])  # This will print 't'

# Nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# Accessing nested elements
print(n_tuple[0][3])  # 's' from "mouse"
print(n_tuple[1][1])  # 4 from the list

# Slicing
print("Sliced:", my_tuple[1:4])  # Elements from index 1 to 3

# Iterating through tuple
for letter in (my_tuple):
    print("Hello", letter)

