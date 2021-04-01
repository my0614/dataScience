import pandas as pd

df = pd.read_csv('./enrolment.csv')

# 코드를 작성하세요.
df['room assignment'] = 'Empty room'
size = df['room assignment'] == 'Empty room'
df.loc[df['status'] == "not allowed", "room assignment"] = "not assigned"
df.loc[size, "room assignment"].value_counts()
# 정답 출력
value = df['room assignment'] == 'Empty room'
count = df.loc[value, "course name"].value_counts() # allowed의 개수

small = list((count[count>=5].index) &(count[count<15].index))
medi = list((count[count>=15].index) &(count[count<40].index))
large = list((count[count>=40].index) &(count[count<80].index))
audi = list(count[count<=80].index)
print(small)
for course in small:
    df.loc[df["course name"] == course, "room assignment"]= "Small room"

for course in medi:
    df.loc[df["course name"] == course, "room assignment"]= "Medium room"

for course in large:
    df.loc[df["course name"] == course, "room assignment"]= "Large room"

for course in audi:
    df.loc[df["course name"] == course, "room assignment"]= "Auditorium"
    
    
print(df)
