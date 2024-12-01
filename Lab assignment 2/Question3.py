import csv
data = [
    {"Name": "ABC", "Age": 28, "City": "Mathura"},
    {"Name": "BCD", "Age": 34, "City": "Agra"},
    {"Name": "CDE", "Age": 25, "City": "Varanasi"},
]
path = 'F:/GLA 1st Sem LAB/Python/Lab assignment 2/Q3.csv'
with open(path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
with open(path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
