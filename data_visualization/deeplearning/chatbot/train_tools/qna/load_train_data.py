import pymysql
import openpyxl

from test import *

def all_clear_train_Data(db):
    sql = '''
    delete from chatbot_train_data
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)

    sql = '''
    ALTER TABLE chatbot_train_data AUTO_INCREMENT = 1
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)
def insert_data(db, xls_row):
    intent, ner, query, answer, asnwer_img_url = xls_row
    sql = '''
    INSERT chatbot_train_Data(intent, ner, query, answer, answer_image)
    values('%s','%s','%s','%s','%s')
    ''' %(intent.value, ner.value, query.value, answer.value, asnwer_img_url.value)

    sql = sql.replace("None", "null")
    with db.cursor() as cursor:
        cursor.execute(sql)
        #print('{} 저장'.format(query.value))
        db.commit()
train_file = './train_data.xlsx'
db = None
try:
    db = pymysql.connect(
    user='root',        
    passwd='1234',
    host="127.0.0.1",
    db='test',
    charset='utf8'
    )
    all_clear_train_Data(db)
    wb = openpyxl.load_workbook(train_file)
    sheet = wb['Sheet1']
    for row in sheet.iter_rows(min_row = 2):
            insert_data(db, row)
    wb.close()
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
        print('success')
