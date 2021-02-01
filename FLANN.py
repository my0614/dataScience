import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import matplotlib.pyplot as pp
import time

#이미지 만들어주는 함수
def make_img(img):
    a = cv2.imread(img)
    img = cv2.resize(a,(300,300))
    return img

def file_cnt(path):
    x = 0
    for pack in os.walk(path):
        for f in pack[2]:
            x +=1
    return x


COLOR = [0,0,0] # 테투리색 정하기
pixel = 15
input_ = input() # 이미지 파일 입력
start = time.time()
qimg = make_img(input_)
constant = cv2.copyMakeBorder(qimg, pixel, pixel, pixel, pixel, cv2.BORDER_CONSTANT, value=COLOR)
qimg = constant
res1, res2 = None, None

#sift 연산
sift = cv2.xfeatures2d.SIFT_create()
kp1,des1 = sift.detectAndCompute(qimg,None)
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks= 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)



index = 0 # 딕셔너리 key값 변수
cnt = 1
count = 0
result = []
img_add = {}
img_dict = {}
index_max = 0

# 원하는 디렉토리의 파일의 개수 가져오기

x = file_cnt('C:/Users/damons/Desktop/img/Abstract_Mosaic_Racerback_Dress')
for i in range(1,x+1):
    index = int(i)
    timg = make_img('C:/Users/damons/Desktop/img/Abstract_Mosaic_Racerback_Dress/img_%08d.jpg' % cnt)
    cnt += 1
    kp2,des2 = sift.detectAndCompute(timg,None)

    matches1 = flann.knnMatch(des1, des2, k=2) # qimg, timg 를 비교하기

    matchesMask = [[0,0] for i in range(len(matches1))]

    for i,(m,n) in enumerate(matches1):
        if m.distance <0.89*n.distance: #ratio 정확도
            matchesMask[i] = [1.0]
            count += 1
    img_add[index] = count # 딕셔너리로 쉽게 비슷한 이미지 찾기
    img_dict.update(img_add)
    
    result.append(count) # 정확도 결과리스트에 추가
    count = 0 # 카운트 초기화
    draw_params = dict(matchColor = (255,0,139),singlePointColor = (255,0,139), matchesMask = matchesMask, flags = 0)
    res1 = cv2.drawMatchesKnn(qimg, kp1, timg, kp2, matches1, res1,  **draw_params)
    #plt.imshow(res1)
    #plt.show()


h_list = []
kidx = 0
set_list = set(result)
result = list(set_list)

for idx in range(0,5):
    print(sorted(result, reverse = True)[idx])
    for key, value in img_dict.items():
        if sorted(result, reverse = True)[idx] == value:
            kidx = key
            fileName = r'C:/Users/damons/Desktop/img/Abstract_Mosaic_Racerback_Dress/img_%08d.jpg' % int(kidx)
            re_img = make_img(fileName)
            constant = cv2.copyMakeBorder(re_img, pixel, pixel, pixel, 7, cv2.BORDER_CONSTANT, value=COLOR) # src, top,bottom, left,right
            
            h_list.append(constant) 


hstack_img = np.hstack((qimg, h_list[0],h_list[1],h_list[2],h_list[3],h_list[4])) # 유사한 이미지 5개한번에 출력
print(time.time() - start)
cv2.imwrite("copy.jpg", hstack_img);
plt.imshow(hstack_img)
plt.show()
