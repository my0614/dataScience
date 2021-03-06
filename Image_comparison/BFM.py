import cv2
import numpy as np
from matplotlib import pyplot as plt

size = int(input('원하는 사진의 크기를 적어주세요. ex) 300  ')) # 사진의 크기 지정해주기
input_path = input('원하는 이미지 파일 경로를 적어주세요.') # 원하는 이미지 파일 경로 지정해주기

# 이미지 비교 class
class compareImg:
    #기본 init 함수
    def __init__(self):
        pass
    
    # 이미지 읽는 함수
    def readImg(self, filepath):
        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE) # 흑백으로 변경
        return img

    # 두개의 이미지 파일 비교
    def diffImg(self,img1, img2):

        # 이미지 파일 사이즈 맞추기 (다르면 오류가 생길수 있음)
        re_img1 = cv2.resize(img1,(size,size))
        re_img2 = cv2.resize(img2, (size,size))
        

        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(re_img1, None)
        kp2, des2 = orb.detectAndCompute(re_img2, None)

        # NROM_HAMMING 2진 문자열 방식이기 때문에 사용한다.
        # crossCheck는 이미지 두개가 비교하여 결과가 같은지 추출하는 옵션
        #BFMathcher은 가장 일치하는것만 반환한다.
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) 

        # 이미지 크기의 사이즈 출력해주기
        print(re_img1.shape[0],re_img1.shape[1])
        print(re_img2.shape[0],re_img2.shape[1])
        # 두개의 이미지에서 공통점 찾기
        matches = bf.match(des1, des2)
        
        # 거리에 따라서 각각의 이미지 매칭시키기
        matches = sorted(matches, key = lambda x:x.distance)


        bf = cv2.BFMatcher()
        #초기값으로 파라미터지정
        matches = bf.knnMatch(des1, des2, k=2)
        good = []
        #ratio 사용하여 특징점찾기 (ratio가 높을수록 정확도가 높음)
        for m,n in matches:
            if m.distance < 0.88 * n.distance:
                good.append([m])
        

        knn_image = cv2.drawMatchesKnn(re_img1, kp1, re_img2, kp2, good, None, flags = 2)
        plt.imshow(knn_image)
        plt.show()
    
    def run(self):
        filepath1 = input_path
        filepath2 = './ring/ring1.jpg'

        img1 = self.readImg(filepath1)
        img2 = self.readImg(filepath2)

        self.diffImg(img1,img2)

if __name__ == '__main__':
    clmg = compareImg()
    clmg.run()

