import ast
input_str = input("Enter a list in the format [1,2,3,'hello',[1,2,2]]: ")
a = ast.literal_eval(input_str)

print(f"The input list is: {a}")
print(f"Type of the input: {type(a)}")
