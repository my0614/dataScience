import csv
import pymysql
import matplotlib.pyplot as plt

size = int(input())
result=  []

f = open('world_cities.csv')
data = csv.reader(f)
next(data)


cities_db = pymysql.connect(
    user='root',
    passwd='1234',
    host="127.0.0.1",
    db='test',
    charset='utf8'
)

cursor = cities_db.cursor(pymysql.cursors.DictCursor) #딕셔너리형태
sql = "SELECT * FROM cities;"
cursor.execute(sql)
cursor.fetchall()
n = -1
label =[]

sql = "truncate test.cities;" #테이블값 전체 삭제
cursor.execute(sql)
cursor.fetchall()
for row in data:
    
    if size <= int(row[3]): #인구별로
        n=n+1
        con = row[1]
        pop = row[3]
        area = row[4]
        result.append(int(row[3])) # 인구그래프
        label.append(row[2])
        sql_in = "insert into test.cities(number,country,population,area)VALUES(%s,%s,%s,%s);"
        val = (n,con,pop,area)
        cursor.execute(sql_in,val)
        cursor.fetchall()

cities_db.commit()
plt.title('Country population')
plt.plot(result,label='population', labels=label)
plt.legend()
plt.show()