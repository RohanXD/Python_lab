#a.	Python Program to Add a Key-Value Pair to the Dictionary

a=int(input("Enter Number of records:"))
my_dict={}
for i in range(1,a+1):
    roll_no=int(input("Enter Roll_no:"))
    name = input("Enter Name:")
    marks = int(input("Enter Marks:"))
    my_dict[i]={"Roll_no":roll_no,"Name":name,"Marks":marks}
print(my_dict)