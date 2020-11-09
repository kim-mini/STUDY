import sys
import numpy as np
import cv2

path = "/home/ubuntu/PycharmProjects/opencv/OpenCV_Python/data/sample_1109.jpeg"
src = cv2.imread(path)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.resize(src, dsize=(500,500))
w, h = 200, 300
dstQuad = np.array([[122, 152], [264, 125], [239, 305], [401, 250]], np.float32)
dst2Quad = np.array([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(dstQuad, dst2Quad)
dst2 = cv2.warpPerspective(dst, pers, (w, h))

cv2.imshow('src', dst)
cv2.imshow('dst', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
