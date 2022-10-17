import numpy as np
import cv2 as cv

def affine_translation():
    src = cv.imread('soodal.jpeg')

    if src is None:
        print('Image load failed')
        return

    affine_mat = np.array([[1, 0, 150],
                           [0, 1, 100]]).astype(np.float32)

    dst = cv.warpAffine(src, affine_mat, (0,0))

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

affine_translation()
