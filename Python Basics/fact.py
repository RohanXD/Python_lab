a=int(input("Enter a Number:"))
fact=1
if a==0:
    print("Factorial doesn't Exist:")
elif a==1:
    print("Factorial = 1")
else:
    for i in range (1,a+1):
        fact*=i
    print("Factorial of",a,"is:",fact)
