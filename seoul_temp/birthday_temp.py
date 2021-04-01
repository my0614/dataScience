import matplotlib.pyplot as plt
import csv

f = open('seoul.csv')
data= csv.reader(f)
high = []
low = []
result = []

a=0
for row in data:
    if row[-1] != '' and row[-2] != '':
        date = row[0].split('-')
        if date[0] == '2002':
            high.append(float(row[-1]))
            low.append(float(row[-2])) 

plt.title('my birthday')
plt.plot(high, 'purple')
plt.plot(low, 'red')
plt.show()