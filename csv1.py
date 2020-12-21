import pandas as pd

df = pd.read_csv('./iphone.csv',index_col = 0)
print(df)
print(df.loc['이름'])