import matplotlib.pyplot as plt
import csv

country = input() 
f = open('age.csv')
data = csv.reader(f)
result = []

for row in data:
    if country in row[0]:
        for i in row[3:]:
            result.append(int(i.replace(',' , '')))  #천단위쉼표 지우기


print(result)
print(sorted(result))
plt.plot(result)
plt.show()