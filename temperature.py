import pymysql
import matplotlib.pyplot as pyplot
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

sql = "truncate test.temp;" #테이블값 전체 삭제
cursor.execute(sql)
cursor.fetchall()

for row in data:
    cnt = row[0]
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