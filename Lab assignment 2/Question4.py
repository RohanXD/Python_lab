my_list = [10, 20, ['Name',60,'Age'], 40, 50]
i = int(input("Enter Index:"))
try:
    element = my_list[i]
    print(f"Element at index {i}: {element}")
except IndexError:
    print(f"Error: Index {i} is out of range for the list.")