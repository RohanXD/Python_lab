def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = int(input("Enter the position in the Fibonacci sequence: "))
if num <= 0:
    print("Input must be a positive integer.")
else:
    print(f"The Fibonacci number at position {num} is {fibonacci(num)}")
