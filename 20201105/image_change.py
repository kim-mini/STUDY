import cv2
import os
from image_effect import *

path = '/home/ubuntu/test/dogs/dogs_3.jpg'

if os.path.isfile(path): # path의 경로에 존재하는지 확인
    img = cv2.imread(path)
else:
    print("not found")


actResize = 0
actRotate = 1
actBlur = 1
actCrop = 1

src = img


def Resize(img):  # 이미지 리사이즈
    src = img
    size = (256, 256)
    dst = cv2.resize(src, dsize=size, interpolation=cv2.INTER_AREA)
    return dst

def Rotate(img): #이미지 로테이션
    height, width, channel = img.shape
    matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
    dst = cv2.warpAffine(img, matrix, (width, height))
    return dst

def Blur(img): #이미지 블러
    src = img
    blur = cv2.GaussianBlur(src,(5,5),0)
    return blur

def Crop(img):  # 이미지크롭
    src = img
    dst = src.copy()
    dst = src[50:130, 100:180]
    return dst

#effect = imageEffect()


if actResize:
    src = Resize(src)

if actRotate:
    src = Rotate(src)

if actBlur:
    src = Blur(src)

if actCrop:
    src = Crop(src)


cv2.imshow("dogs",src)
cv2.waitKey()
cv2.destroyAllWindows()
