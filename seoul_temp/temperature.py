import pymysql
import matplotlib.pyplot as plt
import csv
import math

f = open('seoul.csv')
data = csv.reader(f)
next(data)

#테이블생성
temp_db = pymysql.connect(
    user='root',
    passwd='1234',
    host="127.0.0.1",
    db='test',
    charset='utf8'
)

cursor = temp_db.cursor(pymysql.cursors.DictCursor)
sql = "SELECT * FROM temp;" #temp table 찾기
cursor.execute(sql)
cursor.fetchall()

cnt = ''
result = []

sql = "truncate test.temp;" #테이블값 전체 삭제
cursor.execute(sql)
cursor.fetchall()

year = input()
for row in data:
    if row[0].split('-')[0] == year:
        #print(row[0].split('-')[1] == month)
        cnt = row[0]
        result.append(row[4])
        sql_in = "insert into test.temp(date,avg_temp,min_temp,max_temp)VALUES(%s,%s,%s,%s);"
        if row[2] == '':
            avg = 0
        else:
            avg = math.ceil(float(row[2]))
        if row[3] =='':
            min = 0
        else:
            min = math.ceil(float(row[3]))
        if row[4] =='':
            max = 0
        else:
            max = math.ceil(float(row[4]))
        val = (cnt,avg,min,max)
        cursor.execute(sql_in,val)
        cursor.fetchall()
        #print(row[0],row[2],row[3],row[4])
    
print('success!')
temp_db.commit()
cnt = ''
print(result)
result.sort()
plt.title('%s'%year)
plt.plot(result, label ='tempuerature', color = 'purple')
plt.legend()
ax = plt.gca()
#ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.show()