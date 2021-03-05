from wordcloud import WordCloud
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import re,time
from threading import Thread

def crow():
    print('crow')
    source = requests.get('https://www.bithumb.com/').text
    soup = BeautifulSoup(source, "html.parser")
    hotkeys = soup.select(".sort_coin_box") #class가지고 오기
    price = soup.select(".sort_real")
    print(len(hotkeys))
    for i in range(1,len(hotkeys)):
        a = str(hotkeys[i].text).split(' ')[0]
        print(str(a),str(price[i].text))
    time.sleep(1) # 1초 delay


for i in range(5):
    t1 = Thread(target = crow, args=())
    t1.start()
    time.sleep(1)
