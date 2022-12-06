import csv
with open('resources/username.csv') as csvfile:
    csvfile = csv.reader(csvfile)
    for r in csvfile:
        print(r)
