# 0418.py: OpenCV-Python Tutorials 참조
import cv2
import numpy as np
from matplotlib import pyplot as plt


path = "./data/openCV_logo_1109.png"#사진경로
src = cv2.imread(path)#사진 읽어오기


height, width, channel = src.shape
background = np.zeros(shape = (height,width,3), dtype=np.uint8)+100

grayLogo = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)#색상채널변경
ret, mask = cv2.threshold(grayLogo,190,255,cv2.THRESH_BINARY)#mask 추출
mask2 = cv2.bitwise_not(mask)#mask invert

logo = cv2.bitwise_and(src,src, mask = mask2)#logo만 추출
bg = cv2.bitwise_and(background,background, mask = mask)

blur_logomask = cv2.GaussianBlur(mask2,(5,5),0)
#cv2.imshow('logo',logo)
#cv2.imshow('bg',bg)
result = cv2.bitwise_or(bg,logo)

cv2.imshow('result',mask2)
cv2.waitKey(0)
cv2.destroyAllWindows()
