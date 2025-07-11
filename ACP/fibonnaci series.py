def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

def main():
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print([0])
    else:
        print("Fibonacci Series up to", n, "terms:")
        print(fibonacci(n))

if _name_ == "_main_":
    main(12)