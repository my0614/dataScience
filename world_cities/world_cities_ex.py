import pandas as pd
'''
.head() -> 상위테이블 알려준다
.tail() -> 하위테이블 알려준다.
.columns() -> columns 들을 알려준다. 
.info() -> 정보들을 가져온다.
.describe() ->  통계를 모두 보여준다.
.sort_values() -> 원하는것으로 정렬이 가능하다. asending = False로 하면 내림차순
'''
df = pd.read_csv('./world_cities.csv',index_col = 0)
df['result'] = df['Population'] / df['Land area (in sqKm)']
print(df.sort_values(by='result'))
