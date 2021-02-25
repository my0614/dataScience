#광주지역별 범죄현황
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['font.size'] = 10
plt.figure()
plt.grid()
f = open('광주광역시 자치구별 5대 범죄 현황_20191231.csv')
data = csv.reader(f)
next(data)
country = input()
value = []
for row in data:
    if country in row[0]:
        value.append(row[2:])
df = pd.DataFrame(value)

df.columns=['살인', '강도', '강간.강제추행','절도','폭력']
df.index = ['발생건수','검거건수','검거인원','구속','불구속','기타']
df # DataFrame 출력
result = []
for i in value:
    a = list(map(int, i))
    result.append(a)

graph_label = ['살인', '강도', '강간.강제추행','절도','폭력']
for i in range(5):
    plt.plot(result[i], label = graph_label[i])
    plt.legend()
