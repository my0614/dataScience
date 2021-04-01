import matplotlib.pyplot as plt
import csv

f = open('./subwaytime.csv')
data = csv.reader(f)

next(data)
next(data)

mx = [0] * 24
mx_station = [''] * 24
s_in = [0] *24
s_out = [0] * 24


t = int(input())

for row in data:
    row[4:]= map(int, row[4:])
    for j in range(24):
        b = row[5+j*2]
        if b>mx[j]:
            mx[j] = b
            mx_station[j] = row[3] + '('+ str(j+4) + ')'

print(mx_station,mx)
plt.rc('font', family='Malgun Gothic')
plt.bar(range(24),mx)
plt.xticks(range(24), mx_station, rotation= 90) #ratation은 글자 회전
plt.show()