import csv

city = input('Write a city name:')

with open('003 weather.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if city == row[0]:
            print(row[0], row[1])
