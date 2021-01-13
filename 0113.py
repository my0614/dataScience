import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
df = pd.read_csv('age.csv', encoding = 'cp949', index_col = 0)
df= df.div(df['2019년02월_계_총인구수'], axis = 0)
del df['2019년02월_계_총인구수']

print(df)

name = input()
a = df.index.str.contains(name)
df2 = df[a]

df.loc[np.power(df.sub(df2.iloc[0], axis = 1),2).sum(axis=1).sort_values().index[:5]].T.plot()

plt.show()
