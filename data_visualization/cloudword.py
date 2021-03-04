from bs4 import BeautifulSoup
import requests
import pandas as pd
#5페이지만
movie = []
for page in range(1,6):
    source = requests.get("https://movie.naver.com/movie/point/af/list.nhn?&page=%d" % page).text
    soup = BeautifulSoup(source, "html.parser")
    hotkeys = soup.select("a.movie.color_b") #class가지고 오기
    for i in hotkeys:
        movie.append(i.text)

title = {}
df = pd.DataFrame(movie)
a = df.value_counts() # 영화댓글순위
for i in a.items():
    title[str(i[0]).replace(',','').replace("'",'').replace('(','').replace(')','')] = i[1]

print(title)



