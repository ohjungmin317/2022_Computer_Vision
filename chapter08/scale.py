import numpy as np
import cv2 as cv

def affine_scale():
    src = cv.imread('soodal.jpeg')

    if src is None:
        print('Image load is failed')
        return

    dst1 = cv.resize(src, (0,0), fx=4, fy=4, interpolation=cv.INTER_NEAREST) # INTER_NEAREST는 최근점 값을 보여주기에 사진이 선명하기 보다는
    dst2 = cv.resize(src, (1920, 1280))                                         # 계단 처럼 보이게 된다.
    dst3 = cv.resize(src, (1920, 1280), interpolation=cv.INTER_CUBIC)
    dst4 = cv.resize(src, (1920, 1280), interpolation=cv.INTER_LANCZOS4)

    cv.imshow('src', src)
    cv.imshow('dst1', dst1[400:800, 500:900])
    cv.imshow('dst2', dst2[400:800, 500:900])
    cv.imshow('dst3', dst3[400:800, 500:900])
    cv.imshow('dst4', dst4[400:800, 500:900])

    cv.waitKey()
    cv.destroyAllWindows()

affine_scale()