import pymysql
import pymysql.cursors
import logging

class Database:
    def __init__(self, host, user, password, db_name, charset= 'utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.conn = None
    #DB연결
    def connect(self):
        if self.conn != None:
            return
        self.conn = pymysql.connect(
            host= self.host,
            user = self.user,
            password  = self.password,
            db = self.db_name,
            charset = self.charset
        )
    #DB닫기
    def clsoe(self):
        if self.conn is None:
            self.conn = None
            return
        self.conn.close()
        self.conn = None

    #sql구문 실행
    def execute(self, sql):
        last_row_id = -1
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
            self.conn.commit()
            last_row_id = cursor.lastrowid

        except Exception as ex:
            logging.error(ex)

        finally:
            return last_row_id
    def select_one(self, sql):
        result=  None
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        except Exception as ex:
            logging.error(ex)
        finally:
            return result

    def select_all(self, sql):
        result=  None
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
        except Exception as ex:
            logging.error(ex)
        finally:
            return result