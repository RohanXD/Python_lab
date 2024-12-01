# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

a=int(input("Enter range:"))
my_dict={}
for i in range(1,a+1):
    my_dict[i]={i:i*i}
print(my_dict)