n=int(input("Enter a Number:"))
rev=0
while n>0:
    rem=n%10
    n//=10
    rev=(rev*10)+rem
print("Reversed Number:",rev)
