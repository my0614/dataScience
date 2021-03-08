from konlpy.tag import Kkma

kkma = Kkma()

text = "아버지가 방에 들어갑니다"
morphs = kkma.morphs(text) # 형태소 단위로 나누기
print(morphs)

pos = kkma.pos(text) # 품사
print(pos)

nouns = kkma.nouns(text)
print(nouns)

sentences ='오늘 날씨는 어때요? 내일은 덥다던데.'
sentences = kkma.sentences(sentences)
print(sentences)
