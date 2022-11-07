import numpy as np
import cv2 as cv

src = cv.imread('pepper.bmp')

if src is None:
    print('Image load failed')
    exit()

src_ycrcb = cv.cvtColor(src, cv.COLOR_BGR2YCrCb)
ycrcb_planes = cv.split(src_ycrcb)

# cv.imshow('y',ycrcb_planes[0])
# cv.waitKey()

ycrcb_planes = np.asarray(ycrcb_planes)

ycrcb_planes[0] = cv.equalizeHist(ycrcb_planes[0])

dst_ycrcb = cv.merge(ycrcb_planes)
dst = cv.cvtColor(dst_ycrcb, cv.COLOR_YCrCb2BGR)

cv.imshow('src',src)
cv.imshow('dst',dst)
cv.waitKey()
cv.destroyAllWindows()