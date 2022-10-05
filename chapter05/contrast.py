import numpy as np
import cv2 as cv

def contrast():
    src = cv.imread('soodal.jpeg',cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    s = 1.0
    dst = cv.convertScaleAbs(src, alpha=1+s, beta=-128*s)
    
    cv.imshow('src',src)
    cv.imshow('dst',dst)
    cv.waitKey()
    cv.destroyAllWindows()

contrast()