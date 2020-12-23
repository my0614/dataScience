import pandas as pd

'''
값 수정하기
df = pd.read_csv('./iphone.csv',index_col = 0)
df.loc['iPhone 7', '메모리'] = '13.3GB'
print(df)
'''
df = pd.read_csv('./iphone.csv',index_col = 0)
df.loc[:,'서비스지역'] = 'GW'
print(df)