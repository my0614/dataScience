'''
“information technology” 과목은 심화과목이라 1학년은 수강할 수 없습니다.
“commerce” 과목은 기초과목이고 많은 학생들이 듣는 수업이라 4학년은 수강할 수 없습니다.
수강생이 5명이 되지 않으면 강의는 폐강되어 수강할 수 없습니다.
기존 DataFrame에 “status”라는 이름의 column을 추가하고, 학생이 수강 가능한 상태이면 “allowed”, 수강 불가능한 상태이면 “not allowed”를 넣어주세요.

'''

import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 코드를 작성하세요.
df['status'] = 'allowed'
df.loc[(df['year'] == 1) & (df['course name'] == 'information technology'),'status'] = "not allowed"
df.loc[(df['year'] == 4) & (df['course name'] == 'commerce'), 'status'] = 'not allowed'
value = df['status'] == 'allowed'
count = df.loc[value, "course name"].value_counts() # allowed의 개수
print(count)
count = list(count[count<5].index)
for course in count:
    df.loc[df["course name"] == course, "status"]= "not allowed"
# 정답 출력
df