import cv2
import numpy as np
from matplotlib import pyplot as plt



class compareImg:
    def __init__(self):
        

        pass
    
    def readImg(self, filepath):
        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        return img
    
    def diffImg(self,img1, img2):
        re_img1 = cv2.resize(img1,(300,300))
        re_img2 = cv2.resize(img2, (300,300))
        
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(re_img1, None)
        kp2, des2 = orb.detectAndCompute(re_img2, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

        print(re_img1.shape[0],re_img1.shape[1])
        print(re_img2.shape[0],re_img2.shape[1])
        matches = bf.match(des1, des2)
        
        matches = sorted(matches, key = lambda x:x.distance)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        good = []
        for m,n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])
        
        knn_image = cv2.drawMatchesKnn(re_img1, kp1, re_img2, kp2, good, None, flags = 2)
        plt.imshow(knn_image)
        plt.show()
    
    def run(self):
        filepath1 = r'C:/Users/MY/workspace/datascience/public/images/jesus2.jpg'
        filepath2 = r'C:/Users/MY/workspace/datascience/AVR.png'

        img1 = self.readImg(filepath1)
        img2 = self.readImg(filepath2)

        self.diffImg(img1,img2)

if __name__ == '__main__':
    clmg = compareImg()
    clmg.run()