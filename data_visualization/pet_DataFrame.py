import pandas as pd
import csv
f = open('종로구_반려동물등록현황.csv')
data = csv.reader(f)
next(data) # header 없애기
result = []
for row in data:
    result.append(row)
df = pd.DataFrame(result)
df.columns = ['자치구명','법정동명','행정동명','등록동물수','등록품종수','등록소유자수','동물소유자당등록동물수','해당동의등록대행업체수']

#행정동명 기준으로 분류하기
pd.DataFrame(df['행정동명'].value_counts())



