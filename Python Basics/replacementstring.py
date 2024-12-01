input_str = input("Enter a string: ")
words = input_str.split()
for i in range(len(words)):
    if words[i] == 'this':
        words[i] = 'that'
output_str = ' '.join(words)
print(f"The modified string is: {output_str}")