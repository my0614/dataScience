import pandas as pd
'''
.head() -> 상위테이블 알려준다
.tail() -> 하위테이블 알려준다.
.columns() -> columns 들을 알려준다. 
.info() -> 정보들을 가져온다.
.describe() ->  통계를 모두 보여준다.
.sort_values() -> 원하는것으로 정렬이 가능하다. asending = False로 하면 내림차순
'''

'''
몇개의 도시와 나라가 있는지 출력
df = pd.read_csv('./world_cities.csv',index_col = 0)
pop = df['Country']
pop = pop.describe()
'''
'''
-> 인구밀도가 가장 높은 도시 찾기
df = pd.read_csv('./world_cities.csv',index_col = 0)
df['result'] = df['Population'] / df['Land area (in sqKm)']
print(df.sort_values(by='result'))
'''


df = pd.read_csv('./world_cities.csv',index_col = 0)
result = df['Country'].sort_values()
print(result.value_counts().head(30)) # 각각 몇개가 있는지 알수있다.