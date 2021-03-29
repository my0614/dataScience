import pandas as pd

data = pd.read_csv('./한국교통안전공단_자격증.csv',encoding='cp949')
result = []
label_name = []
for i in data:
    result.append(data[str(i)].sum())
    label_name.append(i)
del result[0]
del result[8]

del label_name[0]
del label_name[8]

df = pd.DataFrame(result,columns = ['Certificate'], index = label_name)
max = df['Certificate'].max()
max_name =df.index[df['Certificate'] == max][0]
min = df['Certificate'].min()
min_name =df.index[df['Certificate'] == min][0]

print('가장많은자격증을 취득한 것은',max_name,'취득한 사람의 수는 ',max)
print('가장많은자격증을 취득한 것은',min_name,'취득한 사람의 수는 ',min)
