import csv
import pandas as pd
f = open('enrolment.csv') # 읽어오기
data = csv.reader(f) # 파일읽기
read = []
next(data)
for row in data:
    read.append(row)

df = pd.DataFrame(read)
df.columns= ['id','year','course_name','status']
#print(df['course_name'].value_counts())
df_1 = df[df['year'] == '1'] # 1학년 DataFrame
df_2 = df[df['year'] == '2'] # 2학년 DataFrame
df_3 = df[df['year'] == '3'] # 3학년 DataFrame
g_1 = df_1['course_name'].value_counts()
g_2 = df_2['course_name'].value_counts()
g_3 = df_3['course_name'].value_counts()
print('1학년이 가장 많이 듣는 과목은',g_1.head(1))
print('2학년이 가장 많이 듣는 과목은',g_2.head(1))
print('3학년이 가장 많이 듣는 과목은',g_3.head(1))


