import csv
import pandas as pd

f = open('laptops.csv')
data = csv.reader(f)
result = []
info = {}
info_re = {}
next(data)

#딕셔너리 삭제 함수
def del_dic(val):
    for key, value in info.items():
        if value != val:
            info_re[key] = value

for row in data:
    result.append(row)
df = pd.DataFrame(result)
df.columns = ['brand','model','ram','hd_type','hd_size','screen_size','price','processor_brand','processor_model','clock_speed','graphic_card_brand','graphic_card_size','os','weight','comments']
brand_in = input('brand,model,ram,hd_type,hd_size,screen_size,price,processor_brand,processor_model,clock_speed,graphic_card_brand,graphic_card_size,os,weight,comments.ex)brand ram screen_size').split()
cnt = 0
for i in range(15):
    info[df.columns[i]] = brand_in[cnt]
    cnt += 1

del_dic('0')
cnt = 0
for i in info_re.items():
    print(i[0],i[1])
    df5 = df[df[i[0]] == i[1]]
    print(pd.DataFrame(df5))
