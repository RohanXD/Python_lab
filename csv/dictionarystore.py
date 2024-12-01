my_dict={}
for i in range(1,a+1):
    roll_no=int(input("Enter Roll_no:"))
    name = input("Enter Name:")
    marks = int(input("Enter Marks:"))
    my_dict[i]={"Roll_no":roll_no,"Name":name,"Marks":marks}
print(my_dict)
total_keys = len(my_dict)
total_values = sum(len(v) for v in my_dict.values())

print("Total number of keys:", total_keys)
print("Total number of values:", total_values)