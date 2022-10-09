import numpy as np
import cv2 as cv

# src = cv.imread('rose.bmp', cv.IMREAD_GRAYSCALE)
src = cv.imread('soodal.jpeg',cv.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed')
    exit()

emboss = np.array([[-1, -1, 0],
                   [-1, 0, 1],
                   [0, 1, 1]], np.float32)

dst = cv.filter2D(src, -1, emboss, delta=128) # ddepth = -1 을 지정하게 되면 출력 영상의 깊이는 입력 영상과 같게 설정된다.
# 엠보싱 필터를 구현할 때에는 결과 영상에 128을 더하는 것이 좋음.

cv.imshow('src',src)
cv.imshow('dst',dst)

cv.waitKey()
cv.destroyAllWindows()