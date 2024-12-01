a = [100, 300, 500, "hello", 300, "hello", 400, 300, 500]
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1

print("Input list is:", a)
print("Frequency of elements is:", b)

