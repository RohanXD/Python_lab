n=int(input("Enter limit:"))
n1=0
n2=1
print(n1, n2)
for i in range(3, n + 1):
    n3 = n1 + n2
    print(n3)
    n2=n3
    n1=n2