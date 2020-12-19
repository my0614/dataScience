import  requests
from bs4 import BeautifulSoup
import re
from collections import Counter


source = requests.get("https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC")
soup = BeautifulSoup(source.content, "html.parser")

value = str(re.findall(r"[a-z]+" , str(soup)))

phrase = Counter(value.split(","))

print(phrase.most_common(10))




