import csv

with open('cities.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if 'Berlin' == row["City"]:
            print(row["State"])

