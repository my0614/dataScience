from wordcloud import WordCloud
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

source = requests.get('https://www.bithumb.com/trade/order/BTC_KRW').text
soup = BeautifulSoup(source, "html.parser")
hotkeys = soup.select(".tx_l.tx_link") #class가지고 오기
for name in hotkeys:
    print(str(name.text).split(' ')[0])
#trs = a.find_all('td')
