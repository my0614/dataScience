#제주도 코로나 현황
#제주도 코로나 현황
import pandas as pd
import csv
import matplotlib.pyplot as plt
f = open('제주특별자치도코로나현황.csv')
data = csv.reader(f)
next(data)
confirme = []
date = []
for row in data:
    confirme.append(row[1])
    date.append(row[0])

print(date)
df = pd.DataFrame({'date' : date, 'confirme' : confirme})
df
