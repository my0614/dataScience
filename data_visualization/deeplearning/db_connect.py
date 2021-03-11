import pymysql

db = None
try:
    db = pymysql.connect(
        user='root',
        passwd='1234',
        host="127.0.0.1",
        db='test',
        charset='utf8'
    )
    print('success')
    sql = '''
        CREATE TABLE tb_student(
        id int primary key auto_increment not null,
        name varchar(32),
        age int,
        address varchar(32)
        ) ENGINE= InnoDB DEFAULT CHARSET=utf8
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
        print("db 연결 닫기 성공")


