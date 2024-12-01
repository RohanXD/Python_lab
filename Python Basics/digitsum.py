n=int(input("Enter Number:"))
s=0
while n!=0:
    r=n%10
    s+=r
    n//=10
print("Sum of Digit=", s)

