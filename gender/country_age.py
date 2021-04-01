import matplotlib.pyplot as plt
import csv

f = open('gender.csv')
data = csv.reader(f)

country = input()
next(data)

m = [] # 남자 리스트
f = [] # 여자 리스트
for row in data:
    if country in row[0]:
        for i in row[3:104]:
            m.append(-int(i))
        for j in row[106:]:
            f.append(int(j))

print(m)
print(f)

plt.title('%s 성별 인구분포' %country)
plt.barh(range(101),m, color = 'blue', label = 'male', )
plt.barh(range(101),f , color = 'purple', label ='female')
plt.legend()
plt.show()

