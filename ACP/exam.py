# Exam Eligibility Checker

# Get input from user
name = input("Enter your name: ")
attendance = float(input("Enter your attendance percentage: "))
marks = float(input("Enter your average marks: "))

# Set eligibility criteria
min_attendance = 75.0   # minimum required attendance percentage
min_marks = 40.0        # minimum required average marks

# Check eligibility
if attendance >= min_attendance and marks >= min_marks:
    print(f"\n{name}, you are eligible to take the exam.")
else:
    print(f"\n{name}, you are NOT eligible to take the exam.")
    if attendance < min_attendance:
        print("Reason: Your attendance is below the required 75%.")
    if marks < min_marks:
        print("Reason: Your average marks are below the required 40%.")
