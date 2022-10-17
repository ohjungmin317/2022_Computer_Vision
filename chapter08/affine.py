import numpy as np
import cv2 as cv

def affine_transform():
    src = cv.imread('soodal.jpeg')

    if src is None:
        print('Image load failed')
        return

    rows = src.shape[0]
    cols = src.shape[1]

    src_pts = np.array([[0,0],
                        [cols - 1, 0],
                        [cols - 1, rows - 1]]).astype(np.float32)

    dst_pts = np.array([[50, 50],
                        [cols - 100, 100],
                        [cols - 50, rows - 50]]).astype(np.float32)

    affine_mat = cv.getAffineTransform(src_pts, dst_pts)

    dst = cv.warpAffine(src, affine_mat, (0,0))

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

affine_transform()