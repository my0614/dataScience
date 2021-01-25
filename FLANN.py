import cv2
import numpy as np

size = int(input()) # 사진 크기 지정
a = cv2.imread('./image/ring/ring2.jpg')
b = cv2.imread('./image/ring/ring.jpg')

qimg = cv2.resize(a,(size,size))
timg = cv2.resize(b,(size, size))
res1, res2 = None, None

#sift 연산
sift = cv2.xfeatures2d.SIFT_create()

kp1,des1 = sift.detectAndCompute(qimg,None)
kp2,des2 = sift.detectAndCompute(timg,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks= 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches1 = flann.knnMatch(des1, des2, k=2) # qimg, timg 를 비교하기

matchesMask = [[0,0] for i in range(len(matches1))]

for i,(m,n) in enumerate(matches1):
    if m.distance <0.7*n.distance:
        matchesMask[i] = [1.0]
    
draw_params = dict(matchColor = (255,0,139),singlePointColor = (255,0,139), matchesMask = matchesMask, flags = 0)

res1 = cv2.drawMatchesKnn(qimg, kp1, timg, kp2, matches1, res1,  **draw_params)

cv2.imshow('FLANN', res1)
cv2.waitKey(0)
cv2.destroyAllWindows()
