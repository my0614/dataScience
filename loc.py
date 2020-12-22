import pandas as pd

df = pd.read_csv('./boardcast.csv', index_col=0)
sbs = df['SBS']
chosun = df['TV CHOSUN']
value = sbs < chosun
# 코드를 작성하세요.

print(df.loc[value, ['SBS','TV CHOSUN']])