import pymysql
import pandas as pd

my_db = pymysql.connect(
    user='root',
    passwd='1234',
    host="127.0.0.1",
    db='test',
    charset='utf8'
)

id = 229
number = 2855
passwd ='cute'
age= 99

#cursor객체 생성
cursor = my_db.cursor(pymysql.cursors.DictCursor) #딕셔너리형태로 반환
sql = "SELECT * FROM info;" # Info table 찾기
cursor.execute(sql)
cursor.fetchall()

sql_in = "insert into test.info(id,number,password,age)VALUES(%s,%s, %s,%s);"
cursor.execute(sql_in, (93,1141, 'cute',96)) # primary 값은 중복값이 안된다.
result = cursor.fetchall()

my_db.commit() #데이터베이스 저장
df = pd.DataFrame(result)
print(df)