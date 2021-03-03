import csv
import pandas as pd
import matplotlib.pyplot as plt
f = open('서울시코로나19확진자현황.csv')
data = csv.reader(f)
next(data)
result = []
for row in data:
    result.append(row)

df = pd.DataFrame(result)
df.columns = ['연번', '확진일','환자번호','국적','환자정보','지역','여행력','접촉력','조치사항','상태','이동경로','등록일','수정일','노출여부']
a = df['지역'].value_counts() # 확진수 알기
#a= sorted(a.items(), key = lambda x : x[0])
print('코로나확진자가 많은 지역')
print(a.head(5))
