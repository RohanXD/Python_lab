#	Python Program to Concatenate Two Dictionaries Into One

a = {"a": 1, "b": 2}
b = {"c": 3, "d": 4}
c = a.copy()

for key, value in b.items():
    c[key] = value
print(c)

a.update(b)
print('Updated dictionary:')
print(a)
