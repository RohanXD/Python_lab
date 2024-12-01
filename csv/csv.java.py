import csv
f=open("record.csv", "w", newline="")
a=csv.writer(f)
a.writerow(["Name","Age",'City'])
data=["Rohan","20","Varanasi"]
a.writerow(data)
print("Row made successfully")
f.close()