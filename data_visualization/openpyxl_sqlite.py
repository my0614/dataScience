import sqlite3
import datetime
import openpyxl

filename = "info.xlsx"
data = openpyxl.load_workbook(filename)
print(data)
conn = sqlite3.connect('test.db', isolation_level = None)
sheet = data.worksheets[0]
    
cur = conn.cursor() #cursor생성
cur.execute(("CREATE TABLE IF NOT EXISTS example(id INTEGER PRIMARY KEY, usernae TEXT, email TEXT, phone TEXT, web TEXT, regdate TEXT)"))
result = []
#
cur.execute("DELETE FROM example")
print('ss',sheet.columns)
for row in sheet.rows:
    for a in row:
        print(a.value)
        result.append(a.value)
    cur.execute("INSERT INTO example VALUES(?, ?, ?, '010-3957-5034','www.min.co.kr',?)", (result[0],result[1],result[2],nowDatetime,))
    result = []
