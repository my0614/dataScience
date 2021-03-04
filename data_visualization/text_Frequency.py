file = open('text_ex.txt')
text = file.read() # file 읽기
wordlist = text.split() # 단어 나누기
wordcnt = {} # 딕셔너리 생성
for word in wordlist:
    wordcnt[word] = wordcnt.get(word,0) + 1
    keys = sorted(wordcnt.keys()) # value값으로 정렬
#출력하기
for word in keys:
    print(word ,':', str(wordcnt[word]))