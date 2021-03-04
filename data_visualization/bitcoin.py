from wordcloud import WordCloud
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import re

source = requests.get('https://www.bithumb.com/trade/order/BTC_KRW').text
soup = BeautifulSoup(source, "html.parser")
hotkeys = soup.select(".tx_l.tx_link") #class가지고 오기
for name in hotkeys:
    test = str(name.text).split(' ')[0]
    test_re = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+') #정규식(한글만 사용)
    print(test_re.sub('',test))
