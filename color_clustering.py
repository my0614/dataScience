import numpy as np
import cv2
from matplotlib import pyplot as mp
from sklearn.cluster import KMeans

# 0 means read gray-scale image
img = cv2.imread("C:/Users/damons/Desktop/parastar_color_extractor-main/parastar_color_extractor/img/1981_Graphic_Ringer_Tee/img_00000009.jpg", 0)
cv2.imwrite("input_gray.png", img)
save_name="output.png"
h, w = img.shape
trans_img = [[i, j, img[i, j]] for i in range(h) for j in range(w)]
# 300 iters * pixels, very slow
kmeans = KMeans(n_clusters=20).fit(trans_img) # n_clusters는 색깔을 나누고자 하는 개수를 의미한다. 
trans_img_tag = kmeans.predict(trans_img)
print(kmeans.cluster_centers_)
img_process = np.zeros((h,w,3),dtype="uint8")
for i,e in enumerate(trans_img_tag):
    x, y = divmod(i, w)
    r,g,b = (e&4)/4,(e&2)/2,e&1
    if e&8:
        r,g,b = 0.5, g, b/2
    img_process[x, y]=r*255,g*255,b*255
cv2.imwrite(save_name,img_process,[int(cv2.IMWRITE_JPEG_QUALITY), 100]) #quality 100
cv2.imshow(save_name,img_process)
k = cv2.waitKey(0)
if k==ord('\x1b'): #esc exit
    cv2.destroyAllWindows()
