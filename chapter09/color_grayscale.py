import numpy as np
import cv2 as cv

def color_grayscale():
    src = cv.imread('butterfly.jpg',cv.IMREAD_COLOR)

    if src is None:
        print('Image load failed')
        return

    dst = cv.cvtColor(src,cv.COLOR_BGR2GRAY)

    cv.imshow('src',src)
    cv.imshow('dst',dst)
    cv.waitKey()
    cv.destroyAllWindows()

color_grayscale()