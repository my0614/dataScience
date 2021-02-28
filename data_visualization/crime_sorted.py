import csv

f = open('광주광역시 자치구별 5대 범죄 현황_20191231.csv') # 읽어오기
data = csv.reader(f) # 파일읽기
police = input() # 관서명
index_1 = 0
index_2 = 0
index_3 = 0
index_4 = 0
index_5 = 0
result = []
dic = {}

#key 찾기
def find_key(val):
    for key,value in dic.items():
        if val == value:
            return key

for row in data:
    if police in row[0]: # 원하는 경찰서 입력
        index_1 += int(row[2])
        index_2 += int(row[3])
        index_3 += int(row[4])
        index_4 += int(row[5])
        index_5 += int(row[6])
        
dic = {'살인' : index_1, '강도' : index_2, '강간,강제추행' : index_3,'절도': index_4,'폭력' : index_5}
print('가장 범죄가 많이 일어나는 것은',find_key(max(dic.values())),':',max(dic.values()))
print('가장 범죄가 적게 일어나는 것은',find_key(min(dic.values())),':',min(dic.values()))



