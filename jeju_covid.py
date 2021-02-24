#제주도 코로나 현황
import pandas as pd
import csv
import matplotlib.pyplot as plt
f = open('제주특별자치도코로나현황.csv')
data = csv.reader(f)
next(data)
confirme = []
complete = []
for row in data:
    confirme.append(row[1])
    complete.append(row[6])

print(confirme)
print(complete)
df = pd.DataFrame({'confirme' : confirme})
df = pd.DataFrame({'complete' : complete})

ax = plt.gca()
ax.axes.yaxis.set_visible(False)

plt.plot(confirme,'purple')
plt.plot(complete,'blue')
