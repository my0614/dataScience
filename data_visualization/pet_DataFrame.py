import pandas as pd
import csv
f = open('종로구_반려동물등록현황.csv')
data = csv.reader(f)
next(data) # header 없애기
divide = []
result = []
table = {}

def find_key(val):
    for key,value in table.items():
        if val == value:
            return key
for row in data:
    result.append(row)
    divide.append(row[2])
df = pd.DataFrame(result)
my = set(divide) 
divide = list(my)
pd.DataFrame(df)
for i in divide:
    df = pd.DataFrame(result)
    df.columns = ['자치구명','법정동명','행정동명','등록동물수','등록품종수','등록소유자수','동물소유자당등록동물수','해당동의등록대행업체수']
    pd.DataFrame(df)
    a= df['행정동명'] == i
    df = df[a]
    df = df.astype({'등록동물수':int})
    to = df['등록동물수'].sum() # 원하는 행 합 구하기
    table[i] = to

print(table)
# 결과 출력
print('등록동물수가 가장 많은 행정동은',find_key(max(table.values())),':',max(table.values()))
print('등록동물수가 가장 적은 행정동은',find_key(min(table.values())),':',min(table.values()))
