n=int(input("Enter a Number:"))
rev=0
a=n
while n>0:
    rem=n%10
    n//=10
    rev=(rev*10)+rem
if a==rev:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome ")
