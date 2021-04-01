import csv
f = open('./seoul.csv')
data= csv.reader(f)
header = next(data)
max_temp = -100
max_data = ''
for row in data:a
    if row[-1] == '':
        row[-1] = max_temp
    row[-1] = float(row[-1]) # 현재 데이터의 마지막에서 4번째인 온도들을 숫자로 변환하기
    if max_temp < row[-1]:
        max_data = row[0]
        max_temp = row[-1]
f.close()
print('기온이 가장 높은 날은', max_data,'이고 가장 높은 온도는 ', max_temp)