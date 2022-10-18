import numpy as np
import cv2 as cv

def affine_rotate():
    src = cv.imread('soodal.jpeg')

    if src is None:
        print('Imeage load failed')
        return

    cp = (src.shape[1] / 2, src.shape[0] / 2) # rows 와 cols가 서로 뒤바뀌어서 (x,y) -> (y,x)
    affine_mat = cv.getRotationMatrix2D(cp, 20, 1)

    dst = cv.warpAffine(src, affine_mat, (0,0))

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

affine_rotate()

