# Armstrong Number Checker

# Get input from user
num = int(input("Enter a number: "))

# Save the original number
original_num = num

# Count number of digits
num_digits = len(str(num))

# Calculate the sum of digits raised to the power of num_digits
sum_of_powers = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

# Check if the number is an Armstrong number
if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
