import pandas as pd
import csv
import matplotlib.pyplot as plt
f = open('C:/Users/MY/Desktop/BloodTransfusionServiceCenter.csv')
import matplotlib.font_manager as fm
from matplotlib import rc

#원그래프 만들 때 한글 사용
fontprop = fm.FontProperties(fname=r"C:\Users\MY\workspace\datascience\NanumFontSetup_TTF_ALL(1)/NanumGothicCoding.ttf").get_name()
rc('font', family=fontprop)
data = csv.reader(f)
next(data)
R = []
F = []
M = []
T = []
S = []
for law in data:
    R.append(law[0:1][0])
    F.append(law[1:2][0])
    M.append(law[2:3][0])
    T.append(law[3:4][0])
    S.append(law[4:5][0])

plt.figure(figsize=(10,5))
plt.title('총기층횟수 빈도', FontProperties = fontprop)
ax = plt.gca()
#ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.Xlabel()
plt.hist(F)

