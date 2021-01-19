import csv
import matplotlib.pyplot as plt
import pymysql

f = open('TOEIC.csv')
data = csv.reader(f)
next(data)

gender =[]
RC_avg = 0
LC_avg = 0
LC_value = 0
RC_value = 0
RC = [] # 그래프 변수
LC = [] # 그래프 변수


toeic_db = pymysql.connect(
    user='root',
    passwd='1234',
    host="127.0.0.1",
    db='test',
    charset='utf8'
)

#테이블 불러오기
cursor = toeic_db.cursor(pymysql.cursors.DictCursor) #딕셔너리형태
sql = "SELECT * FROM toeic;"
cursor.execute(sql)
cursor.fetchall()

#테이블값 전체 삭제
sql = "truncate test.toeic;" #테이블값 전체 삭제
cursor.execute(sql)
cursor.fetchall()
n = 0
for row in data:
    n= n+1
    gender = row[0]
    LC_value = int(row[1])
    LC_avg += LC_value
    RC_value = int(row[2])
    RC_avg += RC_value
    LC.append(int(row[1]))
    RC.append(int(row[2]))
    sql_in = "insert into test.toeic(number,gender,LC,RC)VALUES(%s,%s,%s,%s);"
    val = (n,gender,LC_value,RC_value)
    cursor.execute(sql_in,val)
    cursor.fetchall()

print("finish!")
toeic_db.commit()
plt.title('TOEIC SCORE')
plt.plot(LC,label='LC')
plt.plot(RC,label='RC')
plt.legend()
plt.show()
