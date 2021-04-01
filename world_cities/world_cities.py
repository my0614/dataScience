import pandas as pd
'''
사람 만나기를 좋아하는 익중이는 가장 사람이 붐비는 도시로 여행을 가기로 마음 먹었습니다.
주어진 데이터에서, 인구 밀도(명/sqKm) 가 10000 이 넘는 도시는 총 몇 개인지 알아보세요.
'''

df = pd.read_csv('./world_cities.csv',index_col = 0)
print(df['City / Urban area'].describe()) # 나라들의 통계 출력
print(df['Contry'].describe()) # 도시들의 통계