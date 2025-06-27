# data types
# Numeric types
num1 = 10
num2 = 20.5

# sequence types
text = "Hello, python!" # str
fruits = ["apple", "banana", "cherry"] # list / array

# Mapping type JSON // obj

student_info = {
    "name": "Jawad",
    "age": "13",
    "skills": "html",
} # dict / obj

# Boolean type
is_python_fun = True # bool

# //////////////////////operators
# Arithmetic operators
a = 10
b = 3 
print("Addition:",a + b)
print("Subtraction:",a + b)
print("Multiplication:",a + b)
print("Division:",a + b)
print("Modulus:",a + b)

# Concatenation
str1 = "Hello"
str2 = "World"
combined = str1 + "" +str2
print("Concatenated string:", combined) # Output: "Hello World"

#Repetition
repeated = str1 * 3
print("Repeated string":, repeated) # Ouput: HelloHelloHello

# slicing
slice_str = combined[0:5] # Gets the substring "Hello"
print("Sliced string:", slice_str)

# Methods
upper_str = str1.Upper() # converts to "HELLO"
print("Upper case string:", upper_str)

lower_str = str2.lower() # Converts to "world"
print("Lower case string:", lower_str)

# String lenght
print("Lenght of combined string:", len(combined))