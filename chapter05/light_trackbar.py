import numpy as np
import cv2 as cv

def light_trackbar():
    src = cv.imread('soodal.jpeg',cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    def update(pos):
        dst = cv.add(src,pos)
        cv.imshow('dst',dst)

    cv.namedWindow('output')
    cv.createTrackbar('trackbar','output',0 ,100 ,update)
    update(0)

    cv.waitKey()
    cv.destroyAllWindows()

light_trackbar()