import matplotlib.pyplot as plt
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

result = []
for row in data:
    row[4:] = map(int,row[4:]) # map함수를 사용하여 정수로 바꿔주기
    result.append(row[10]) #row[10] 은 출근시간인 7시의 승차 인덱스 

print(len(result))
print(result)
plt.title('subway')
plt.bar(range(len(result)), result, color = 'purple', label = 'people')
plt.legend()
plt.show()