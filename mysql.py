import pymysql
import pandas as pd

my_db = pymysql.connect(
    user='root',
    passwd='1234',
    host="127.0.0.1",
    db='test',
    charset='utf8'
)

#cursor객체 생성
cursor = my_db.cursor(pymysql.cursors.DictCursor) #딕셔너리형태로 반환

sql = "SELECT * FROM info;" # Info table 찾기
cursor.execute(sql)
result = cursor.fetchall()
show = pd.DataFrame(result)
print(show)