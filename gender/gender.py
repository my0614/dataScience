import csv
import matplotlib.pyplot as plt

f = open('gender.csv')
data = csv.reader(f)
next(data)
size = []

country = input('원하는 지역을 적어주세요.')
m=[]
f=[]
for row in data:
    if country in row[0]:
        for i in range(3,104):
            m.append(int(row[i])) #남자라인
            f.append(int(row[i+103])) #여자라인
        break

plt.plot(m, label='male')
plt.plot(f, label = 'female')
plt.legend()
plt.show()


