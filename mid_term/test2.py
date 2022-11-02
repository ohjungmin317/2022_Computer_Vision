import numpy as np
import cv2 as cv

src = cv.imread('tekapo.bmp')

a = src.shape[0]
b = src.shape[1]

# affine_mat = np.array([[1,0,150], [0,1,100]]).astype(np.float32)
# affine_mat = np.array([[1,0.3,0], [0,1,0]]).astype(np.float32)
affine_mat = np.array([[-1,0,b], [0,1,0]]).astype(np.float32)
# affine_mat = np.array([[2,0,0], [0,2,-a]]).astype(np.float32)

dst = cv.warpAffine(src, affine_mat, (0,0))
cv.imshow('dst',dst)
cv.waitKey()