import pandas as pd
    
df = pd.read_csv('./TOEIC.csv')

# 코드를 작성하세요.
df['합격여부'] = (df['LC'] >= 250) & (df['RC'] >= 250) & ((df['LC'] + df['RC']) >= 600)
 
# 정답 출력
print(df)