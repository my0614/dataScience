import matplotlib.pyplot as plt
import csv

f = open('seoul.csv')
data= csv.reader(f)
result  = []
a=0
for row in data:
    if row[-1] != '':
        if row[0].split('-')[0] == '2018':
        #if a[1] == '06': # 6월달 추출하기
            result.append(float(row[-1])) # 6월달의 각 날짜의 최고온도

plt.plot(result, 'purple')
plt.show()



