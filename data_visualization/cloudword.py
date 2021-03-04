from bs4 import BeautifulSoup
import requests

page_url = 'https://news.daum.net/breakingnews/digital'
page_response = requests.get(page_url)
page_soup = BeautifulSoup(page_response.text)
print(page_soup)
select = page_soup.select('.link_txt')
articles = []
#단어 찾기
for link in select:
    article_text = link[0].text
    print(article_text)
    articles.append(article_text.strip().replace('\n', ' '))
print(articles)


