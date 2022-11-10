import numpy as np
import cv2 as cv

def on_trackbar(pos):
    bsize = pos
    if bsize % 2 == 0:
        bsize = bsize - 1
    if bsize < 3:
        bsize = 3

    dst = cv.adaptiveThreshold(src, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, bsize, 5)
    # 기존 이진화 해주는 것보다 적응형 이진화를 해주는 경우에 각 pixel의 사각형별로 이진화를 해주기 때문에 빛에 의한 밝기 차에 대해서도
    # 이진화를 해주어 기존 이진화는 선이 안보이지만 적응형이진화는 선도 보이게 해준다.

    cv.imshow('dst', dst)

src = cv.imread('sudoku.png',cv.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed')
    exit()
cv.imshow('src',src)

cv.namedWindow('dst')
cv.createTrackbar('Block Size', 'dst', 0, 200, on_trackbar)
cv.setTrackbarPos('Block Size','dst', 11)

cv.waitKey()
cv.destroyAllWindows()
