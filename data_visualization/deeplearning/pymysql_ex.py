import pymysql

db= None
try:
    db = pymysql.connect(host='127.0.0.1', user='root',passwd='1234',db='test',charset='utf8')
    
    sql= '''
    CREATE TABLE tb_student(
    id in primary key auto_increment not null,
    ame varchar(32),
    age int,
    address varchar(32)
    ) ENGINE= InnoDB DEFAULT CHARSET = utf8
    '''
    
    with db.cursor() as cursor:
        cursor.execute(sql)
        
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
