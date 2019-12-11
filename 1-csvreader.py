import csv


with open('1-csvin.csv', 'w') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        print(', '.join(row))
