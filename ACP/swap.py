# Get input from user
a = int(input("Enter the first number (a): 10"))
b = int(input("Enter the second number (b): 20"))
c = int(input("Enter the third number (c): 30"))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# Swapping logic
# a -> b, b -> c, c -> a
a, b, c = b, c, a

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
print("c=", c)