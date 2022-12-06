import csv

with open('resources/names.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
    csvwriter.writerow(['Alex', 'Serj', 'Yana'])