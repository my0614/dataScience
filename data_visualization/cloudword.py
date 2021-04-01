from bs4 import BeautifulSoup
import requests
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#5페이지만
movie = []
for page in range(1,22):
    source = requests.get("https://movie.naver.com/movie/point/af/list.nhn?&page=%d" % page).text
    soup = BeautifulSoup(source, "html.parser")
    hotkeys = soup.select("a.movie.color_b") #class가지고 오기
    for i in hotkeys:
        movie.append(i.text)

title = ""
df = pd.DataFrame(movie)
a = df.value_counts() # 영화댓글순위
print(a)
for i in a.items():
    title += str(i[0]).replace(',','').replace("'",'').replace('(','').replace(')','').replace(' ','')+" "

#print(title)
#wordcloud만들기
wordcloud = WordCloud(font_path=r"C:\Users\MY\workspace\datascience\NanumFontSetup_TTF_ALL(1)/NanumGothicCoding.ttf", background_color='purple').generate(title)
#그래프 그리기
plt.figure(figsize=(22,22)) #이미지 사이즈 지정
plt.imshow(wordcloud, interpolation='lanczos') #이미지의 부드럽기 정도
plt.axis('off') #x y 축 숫자 제거
plt.show() 
plt.savefig()
