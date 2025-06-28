# nested if and else
number = int(input("enter a number: "))
if number > 50:
    if number % 2 == 0:
        print("even and greater than 50and it is")
    else:
        print("number is smaller than 50")
else:
    print("number is smaller 50")
        
        
# if-elif-else statement 
marks = int(input("enter your marks : "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")    
else:
    print("Grade: F")    