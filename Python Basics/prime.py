a = int(input("Enter the upper limit to find prime numbers: "))
for i in range(2, a + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)