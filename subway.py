import csv
import matplotlib.pyplot as plt

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)


label = ['유임승차','유임하차','무임승차','무임하차']
color =['purple', 'yellow', 'pink','green']
plt.rc('font', family='Malgun Gothic')


for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
        plt.figure(dpi= 300)
        plt.title(row[3] + '' + row[1])
        plt.pie(row[4:8], labels= label, colors= color, autopct='%.1f%%')
        plt.axis('equal')
        plt.savefig(row[3]+ ' '+row[1]+'.png') # png파일로 저장하기
        plt.show()