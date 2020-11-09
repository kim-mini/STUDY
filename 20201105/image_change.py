import cv2
import os
from image_effect import *

path = '/home/ubuntu/test/dogs'
outpath = '/home/ubuntu/test/output'

if os.path.isdir(path): # path의 경로에 존재하는지 확인
    fileList = os.listdir(path)
else:
    print("not found path")

if os.path.isdir(outpath):  # path의 경로에 존재하는지 확인
    pass
else:
    print("not found outpath")


# 효과 설정
actResize = 0
actRotate = 1
actBlur = 0
actCrop = 1


cnt = 0 #파일의 번호 매겨주기

effect = imageEffect() # 함수가 들어있는 클래스 호출

for filename in fileList:
    path1 = os.path.join(path, filename)
    img = cv2.imread(path1)
    src = img
    print(path1)

    if actResize:
        src = effect.Resize(src)

    if actRotate:
        src = effect.Rotate(src)

    if actBlur:
        src = effect.Blur(src)

    if actCrop:
        src = effect.Crop(src)

    outname = "dogs_%i"%cnt + ".jpg"
    path2 = os.path.join(outpath, outname) // 아웃풋경로
    cv2.imwrite(path2, src) # 해당경로에 해당소스저장
    cnt += 1




cv2.imshow("after", src)
cv2.waitKey()
cv2.destroyAllWindows()
