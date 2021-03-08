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
print(len(review_data))
print('1 말뭉치 데이터 읽기 완료 : ', time.time() - start)

print('2) 형태소 명사만 추출 시작')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) 형태소에서 명사만 추출 완료', time.time() -start)

print('3) word2vec 모델 학습 시작')
model = Word2Vec(sentences=docs,  size = 200, window = 4, hs = 1, min_count = 2, sg = 1)
print('3) 모델 학습 완료', time.time() - start)

print('4) word2vec 모델 학습 저장')
model.save('nvmc.model')
print('4) 모델 저장 완료', time.time() - start)

print(model.corpus_count)
print(model.corpus_total_words)

