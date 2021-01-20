from PIL import Image
import numpy as np

with open('AVR_pinmap.png',"rb") as file: # 이미지파일 열기
    img = Image.open(file) #파일열기
    img = img.convert("RGB") # RGB모드로 변환
    img = img.resize((64,64)) # 크기 정하기
    data = np.asarray(img) # np
    img.save('AVR.png')
    print(data)
