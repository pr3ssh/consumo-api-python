import csv


with open('1-csvout.csv', 'w') as csvfile:
    fieldnames = ['option_1', 'option_2', 'option_3']
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
    csvwriter.writerow(['A, sss', 'B', 'C'])
    csvwriter.writerow(['B', 'A', 'C'])
