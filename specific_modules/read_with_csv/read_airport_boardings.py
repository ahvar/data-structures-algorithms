import csv

with open("./data/airport_boardings.csv", "r") as file_in:
    reader = csv.reader(file_in)
    header = next(reader)
    for row in reader:
        pass

airport_file = open("./data/less_airport_boardings.csv", "r")
airport_reader = csv.reader(airport_file)
header = next(airport_reader)
row = ""
while airport_reader:
    print(row)
    row = next(airport_reader)
