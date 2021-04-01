 # Pickle 모듈
 텍스트 이외의 자료형을 파일로 저장하기 위해서 사용하는 모듈이다.
 
 ## 파일입출력 방법
 파일을 저장하거나 불러올때는 파일을 바이트형식으로 읽거나 써주어야 한다. ex(wb,rb)

### 코드 예시
 '''
 파일을 쓸때에는 pickle.dump()함수를 쓴다. 
 ex) pickle.dump(data, file)

 파일을 읽어올때는 pickle.load()함수를 쓴다.
 ex) pickle.load(file)
 '''