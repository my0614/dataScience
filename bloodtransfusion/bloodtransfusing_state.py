import pandas as pd
import csv
import matplotlib.pyplot as plt
f = open('C:/Users/MY/Desktop/BloodTransfusionServiceCenter.csv')
import matplotlib.font_manager as fm
from matplotlib import rc
label = ['헌혈 O','헌혈 X']
#원그래프 만들 때 한글 사용
fontprop = fm.FontProperties(fname=r"C:\Users\MY\workspace\datascience\NanumFontSetup_TTF_ALL(1)/NanumGothicCoding.ttf").get_name()
rc('font', family=fontprop)
data = csv.reader(f)
next(data)

R = [] # 최근 기증 후 개월
F = [] # 총기증빈도
M = [] # 총기증된 혈액 양
T = [] # 첫 기증 후 개월 수
S = [] # 헌혈 유무 확인

for law in data:
    if law[0:1][0] != '' and law[1:2][0] != '' or law[3:4][0] != '' or law[4:5][0] != '':
        
        if int(law[4:5][0]) == 0:
            no = no+1
        else:
            yes = yes+1

S.append(yes)
S.append(no)
plt.figure(figsize=(10,5))

plt.title('헌혈 유무 확인 그래프', FontProperties = fontprop)
ax = plt.gca()
ax.axes.title.set_size(20)
plt.pie(S,labels=label, autopct='%.1f%%')
