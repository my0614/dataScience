import matplotlib.pyplot as plt
import csv

f = open('seoul.csv')
data= csv.reader(f)
result  = []
for row in data:
    result.append(row[4])

f.close()
plt.plot(result, 'purple')
plt.figure(figsize = (10,2))
plt.show()

