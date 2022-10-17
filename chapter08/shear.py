import numpy as np
import cv2 as cv

def affine_shear():
    src = cv.imread('soodal.jpeg')

    if src is None:
        print('Image load is failed')
        return

    rows = src.shape[0]
    cols = src.shape[1]

    mx = 0.3
    affine_mat = np.array([[1, mx, 0],
                        [0, 1, 0]]).astype(np.float32)

    dst = cv.warpAffine(src, affine_mat, (int(cols + rows *mx), rows))

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

affine_shear()
