
from konlpy.tag import Komoran

#어절나누기
def word_ngram(bow, num_gram):
    text= tuple(bow)
    ngrams= [text[x:x+num_gram] for x in range(0, len(text))]
    return tuple(ngrams)

#유사도 
def similarity(doc1, doc2):
    cnt = 0
    for token in doc1:
        if token in doc2: # doc1안에 들어있는 token이 doc2에도 들어있으면
            cnt = cnt+1
    return cnt/len(doc1)

sen1 = '6월에 뉴턴은 선생님의 제안으로 트리니티에 입학했다.'
sen2 = '6월에 뉴턴은 선생님의 제안으로 대학에 입학했다.'
sen3 = '나는 맛있는 밥을 뉴턴 선생님과 함께 먹었다.'

#명사 추출
komora = Komoran()
bow1 = komoran.nouns(sen1)
bow2 = komoran.nouns(sen2)
bow3 = komoran.nouns(sen3)

#어절 나누기
doc1 = word_ngram(bow1, 2)
doc2 = word_ngram(bow2, 2)
doc3 = word_ngram(bow3, 2)

print(doc1)
print(doc2)

#각각 유사도 검색
r1 = similarity(doc1, doc2)
r2 = similarity(doc1, doc3)

print(r1)
print(r2)
