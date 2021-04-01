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
    for i in range(24):
        s_in[i] += row[4+i*2]
        s_out[i] += row[5+i*2]


print(mx_station,mx)
plt.rc('font', family='Malgun Gothic')
plt.plot(s_in, label= 'In')
plt.plot(s_out, label= 'Out')
plt.show()