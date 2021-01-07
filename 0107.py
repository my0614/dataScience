import matplotlib.pyplot as plt
import csv

f = open('subwaytime.csv')
data = csv.reader(f)

next(data)
next(data)

mx = 0
mx_station = ''

t = int(input())

for row in data:
    row[4:]= map(int, row[4:])
    a = row[4+(t-4)*2]
    if a > mx:
        mx = a
        mx_station = row[3] + '('+ row[1] + ')'

print(mx_station,mx)
