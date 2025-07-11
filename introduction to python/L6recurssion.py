# recurssion 
def countdown(n):
    if n == 4: # Base case 
        print("Goooooo!")
    else:
        print(n)
        countdown(n + 1) # recursive call 

countdown(1)

# factorial 
def factorial(n):
    if n==1: #base call
        return 1
    else:
        return n * factorial(n - 1)

answer = factorial(5)
print(answer)