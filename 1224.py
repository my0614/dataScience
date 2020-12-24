import pandas as pd

df = pd.read_csv('./liverpool.csv',index_col = 0)
df.rename(columns = {'position':'Position'},inplace = True)
df['Player name'] = df.index
df.set_index('number',inplace = True)
print(df)