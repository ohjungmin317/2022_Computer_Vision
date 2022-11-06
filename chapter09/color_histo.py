import numpy as np
import cv2 as cv

def color_histo():
    src = cv.imread('pepper.bmp',cv.IMREAD_COLOR)

    if src is None:
        print('Image load failed')
        return

    src_ycrcb = cv.cvtColor(src,cv.COLOR_BGR2YCrCb)

    ycrcb_planes = cv.split(src_ycrcb)

    ycrcb_planes[0] = cv.equalizeHist(ycrcb_planes[0])

    dst_ycrcb = cv.merge(ycrcb_planes)

    dst = cv.cvtColor(dst_ycrcb, cv.COLOR_YCrCb2BGR)

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

color_histo()