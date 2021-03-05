from wordcloud import WordCloud
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import re
import threading, time
def crow():
    source = requests.get('https://www.bithumb.com/').text
    soup = BeautifulSoup(source, "html.parser")
    hotkeys = soup.select(".sort_coin_box") #class가지고 오기
    price = soup.select(".sort_real")
    print(len(hotkeys))
    for i in range(1,len(hotkeys)):
        print(str(hotkeys[i].text),str(price[i].text))
crow()
