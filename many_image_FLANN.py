import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import matplotlib.pyplot as pp

print("hello")
input_ = input() # 이미지 파일 입력

a = cv2.imread(input_)
qimg = cv2.resize(a,(300,300))

res1, res2 = None, None

#sift 연산
sift = cv2.xfeatures2d.SIFT_create()

kp1,des1 = sift.detectAndCompute(qimg,None)


FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks= 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)


x = 0
cnt = 1
count = 0
result = []
index_max = 0
# 원하는 디렉토리의 파일의 개수 가져오기
for pack in os.walk('C:/Users/damons/Desktop/workspace/Datamonsters/image/fasion/'):
    for f in pack[2]:
        x +=1
print('file count = ',x)
for i in range(1,x+1):
    b = cv2.imread('./image/fasion/fasion_%d.jpg' % cnt)
    cnt +=1
    timg = cv2.resize(b,(300, 300))
    kp2,des2 = sift.detectAndCompute(timg,None)
    matches1 = flann.knnMatch(des1, des2, k=2) # qimg, timg 를 비교하기

    matchesMask = [[0,0] for i in range(len(matches1))]

    for i,(m,n) in enumerate(matches1):
        if m.distance <0.89*n.distance:
            matchesMask[i] = [1.0]
            count += 1
    
    result.append(count) # 정확도 결과리스트에 추가
    count = 0 # 카운트 초기화
    draw_params = dict(matchColor = (255,0,139),singlePointColor = (255,0,139), matchesMask = matchesMask, flags = 0)
    res1 = cv2.drawMatchesKnn(qimg, kp1, timg, kp2, matches1, res1,  **draw_params)
    plt.imshow(res1)
    plt.show()

print(result)
index_max = result.index(max(result))
print(index_max)
fileName = r'C:/Users/damons/Desktop/workspace/Datamonsters/image/fasion/fasion_%d.jpg' % index_max
ndarray = img.imread(fileName)
plt.imshow(ndarray)
plt.show()
