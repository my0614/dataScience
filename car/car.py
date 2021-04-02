import csv

f = open('car.csv')
data = csv.reader(f)

country = input() #지역가져오기
for row in data:
    if country in row[33]:
        print(row[0], row[30])