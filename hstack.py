import cv2
import numpy as np

cat_img = cv2.imread("./image/fasion/fasion_14.jpg")
print("cat_img.shape = {0}".format(cat_img.shape))
hstack_cat = np.hstack((cat_img, cat_img))
print("hstack_cat.shape = {0}".format(hstack_cat.shape))

cv2.imshow("hstack_cat",hstack_cat)
cv2.waitKey()
