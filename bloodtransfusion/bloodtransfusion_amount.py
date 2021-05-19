import csv
import numpy as np
import matplotlib.pyplot as plt
f = open('C:/Users/MY/Desktop/BloodTransfusionServiceCenter.csv') # 파일경로 나타내기
import matplotlib.font_manager as fm
from matplotlib import rc

# 그래프 만들 때 한글 사용
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
        M.append(int(law[2:3][0]))
        F.append((law[1:2][0]))

plt.figure(figsize=(10,5))
plt.title('기증횟수를 사용하여 총 수혈의 양 나타내기', FontProperties = fontprop)
N = 1
color = np.random.rand(N)
plt.scatter(M,F, c= 'purple',alpha=0.5)
ax = plt.gca()
ax.axes.title.set_size(20)
#ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

