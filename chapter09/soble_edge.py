import cv2 as cv
import numpy as np

def sobel_edge():
    src = cv.imread('lenna256.bmp',cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    dx = cv.Sobel(src, cv.CV_32F,1,0) # x에 대한 편미분
    dy = cv.Sobel(src, cv.CV_32F,0,1) # y에 대한 편미분

    fmag = cv.magnitude(dx, dy)
    mag = np.uint8(np.clip(fmag,0,255))
    _, edge = cv.threshold(mag, 150, 255, cv.THRESH_BINARY) # 255 보다 값을 크게 되면 150으로 변환 -> 150 보다 크게 되면 에지로 판단
    # 임계값을 150보다 낮추게 되면 더 많은 에지 픽셀이 edge 영상에서 나타나게 된다. => 단 잡음의 영향도 에지로 검출이 될 수도 있다.

    cv.imshow('src',src)
    cv.imshow('mag',mag)
    cv.imshow('edge',edge)
    cv.waitKey()
    cv.destroyAllWindows()

sobel_edge()