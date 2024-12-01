try:
    a = input("Please enter an integer: ")
    int_a = int(a)
    if int_a:
        print ("You are Entered a valid Number")
    else:
        raise ValueError
except ValueError:
    print(f"Invalid Integer")
