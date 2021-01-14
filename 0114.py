import matplotlib.pyplot as plt
import csv
import matplotlib.font_manager as fm

font_path = r'./NanumFontSetup_TTF_ALL(1)/NanumGothicCoding.ttf'
fontprop = fm.FontProperties(fname= font_path, size = 12)
f = open('bike.csv')
data = csv.reader(f)

next(data)

result = [] #리스트생성
label = []
country = input() #원하는 지역 입력받기

for row in data:
    if country in row[1]:
        print(row[1])
        result.append(row[5]) #보관대수 결과로
        label.append(row[0]) # 보관수명

result.sort()
print(result)
plt.plot(result, label = 'bike count', color = 'purple')

plt.xlabel('보관대수', FontProperties = fontprop)
plt.ylabel('자전거', FontProperties = fontprop)
plt.title('%s Bike Storage count' % country, FontProperties = fontprop)
plt.legend()
plt.show()
