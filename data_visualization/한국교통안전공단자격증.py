import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc

data = pd.read_csv('./한국교통안전공단_자격증.csv',encoding='cp949')

fontprop = fm.FontProperties(fname=r"C:\Users\MY\workspace\datascience\NanumFontSetup_TTF_ALL(1)/NanumGothicCoding.ttf").get_name()
rc('font', family=fontprop)


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

x = np.arange(3)
plt.figure(figsize=(12, 3))
plt.bar(label_name,result)
plt.show()

