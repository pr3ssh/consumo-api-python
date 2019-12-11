import csv


people = [
        {'first_name': 'Pablo', 'last_name': 'Martín'},
        {'first_name': 'Miguel Ángel', 'last_name': 'Rodríguez'},
        {'first_name': 'Gonzalo', 'last_name': 'Aranda'}
        ]

with open('1-dictwriter.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for p in people:
        writer.writerow(p)
