import os

def character(dir):
    letters = []
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            filepath = os.path.join(dir, file)
            with open(filepath, 'r') as file:
                content = file.read()
                letters.extend(list(content))

    return letters
file_path = 'F:/GLA 1st Sem LAB/Python/Lab assignment 2'
char_list = character(file_path)
print(char_list)
