#광주지역별 범죄현황
import pandas as pd
import csv
import matplotlib.pyplot as plt
f = open('광주광역시 자치구별 5대 범죄 현황_20191231.csv')
data = csv.reader(f)
next(data)
country = input()
list = []
for row in data:
    if country in row[0]:
        list.append(row[2:])
df = pd.DataFrame(list)

df.style.set_caption("Hello World")
df.columns=['살인', '강도', '강간.강제추행','절도','폭력']
df.index = ['발생건수','검거건수','검거인원','구속','불구속','기타']
df
