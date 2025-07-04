for i in range(1, 6): # outer loop for rows
    for j in range(1, 6): # inner loop for columns
        print(f"{i + j}", end="\t")
    print() # Move to next line

    # simple way 
number = 2
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")







for i in range(1, 6): #row
    for j in range(1, 1+1): #col
        print("*", end="")
    print()