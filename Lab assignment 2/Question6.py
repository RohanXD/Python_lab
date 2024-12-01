try:
    n = float(input("Enter the numerator: "))
    d = float(input("Enter the denominator: "))

    div = n / d
    print(f"The result of the division is: {div}")
except ArithmeticError as e:
    print(f"An arithmetic error occurred: {e}")
