from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time

def read_review_data(filename):
    with open(filename, 'r', encoding='UTF-8') as f: # 파일열기
        data = [line.split('\t') for line in f.read().splitlines()]
        data= data[1:]
    return data

start = time.time()

print('1 말뭉치 데이터 읽기')
review_data = read_review_data('./ratings.txt')
rint('2) 형태소 명사만 추출 시작')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) 형태소에서 명사만 추출 완료', time.time() -start)