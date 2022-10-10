import numpy as np
import cv2 as cv

def unsharp():
    src = cv.imread('soodal.jpeg',cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load faield')
        return

    cv.imshow('src',src)

    for sigma in range(1, 6):
        blurred = cv.GaussianBlur(src,(0,0), sigma)

        alpha = 1.0
        dst = cv.addWeighted(src, 1+alpha, blurred, -alpha, 0,0)

        desc = "sigma : %d" %(sigma)
        cv.putText(dst, desc, (10,30), cv.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv.LINE_AA)

        cv.imshow('dst',dst)
        cv.waitKey()

    cv.destroyAllWindows()

unsharp()