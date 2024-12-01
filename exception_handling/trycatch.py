# try, except , else , finally

try:
    a = int(input("Enter a Number:"))
    b = 4 / a
    print(b)
    raise IndexError
except ZeroDivisionError:
    print("Division by Zero")
except ValueError:
    print("hjdfijn")
else:
    print("It is a Error")
finally:
    print("aa gya finally")
