import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table',header=0, index_col =0)

summer = df[1].iloc[:,:5]
summer.columns = ['Play','Gold','Sliver','Dong','Result']

print(summer.sort_values('Gold', ascending = False))
summer.to_excel('summer olympic.xlsx')