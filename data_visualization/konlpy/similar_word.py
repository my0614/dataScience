from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time
from random import *

def read_review_data(filename):
    with open(filename, 'r', encoding='UTF-8') as f: # 파일열기
        data = [line.split('\t') for line in f.read().splitlines()]
        data= data[1:]
    return data

start = time.time()

print('1 말뭉치 데이터 읽기')
review_data = read_review_data('./ratings.txt')
print(len(review_data))
print('1 말뭉치 데이터 읽기 완료 : ', time.time() - start)

print('2) 형태소 명사만 추출 시작')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) 형태소에서 명사만 추출 완료', time.time() -start)


model = Word2Vec(sentences = docs, size = 200, window = 4, hs =1, min_count = 2, sg = 1)
model.save('nvmc.model')

end = 0
a = randint(0, len(docs))
print(a)
print('주어진 단어', str(docs[a]))
word = ''
word = str(docs[a][0])
print(word)



model = Word2Vec.load('nvmc.model')
print(model.corpus_total_words)

while end == 0:
    word2= input()
    score = model.wv.similarity(word,word2)
    if score <= 0.1:
        print('유사한 단어가 아닙니다.')
        exit(0)
    print(score)

