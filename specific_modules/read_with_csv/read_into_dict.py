
import csv

with open("/Users/arthurvargas/dev/pyreview/data/ACSST1Y2023.S0101-2025-01-06T173644.csv", newline='', encoding='utf-8-sig') as file_in:
    reader = csv.DictReader(file_in)
    for line in reader:
        print(line["United States!!Total!!Estimate"])