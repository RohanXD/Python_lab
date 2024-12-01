import csv
def csv_dict(path):
    with open(path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data_list = []
        for row in csv_reader:
            data_list.append(dict(row))
    return data_list
file_path = 'F:/GLA 1st Sem LAB/Python/Lab assignment 2/Q2.csv'
data = csv_dict(file_path)
print(data)
