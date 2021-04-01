import cv2

img = cv2.imread('./image.png')
print(img.shape)

imresize = cv2.resize(img,(500,500)) # 이미지 크기 resize 맞추기

imgcrop = imresize[150:350, 150: 350] # 원하는 부분 가지고오기(resize를 중심으로 가운데)
cv2.imshow('resize',imresize)
cv2.imshow('crop',imgcrop)
cv2.waitKey(0)
