
import matplotlib.pyplot as plt
import csv

f = open('./subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

result = []


for row in data:
    row[4:] = map(int,row[4:]) # map함수를 사용하여 정수로 바꿔주기
    result.append(row[10])

print(result)
plt.bar(range(len(result)), result)
plt.show()
