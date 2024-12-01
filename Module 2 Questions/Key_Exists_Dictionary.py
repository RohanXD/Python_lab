#Python Program to Check if a Given Key Exists in a Dictionary or Not

a = {"a": 1, "b": 2}
if 'c' in a:
    print("Key Does not exist")
b = {"c": 3, "d": 4}
if 'c' in b:
    print("Key Does exist")
c = a.copy()

for key, value in b.items():
    c[key] = value
print(c)
if 'c' in c and 'd' in c:
    print("Key exist in both")