num_str = input("Enter numbers: ")
new=num_str.split()
odd_sum = 0
for i in new:
    i = int(i)
    if i % 2 != 0:
        odd_sum += i
print(f"The sum of odd numbers is: {odd_sum}")