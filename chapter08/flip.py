import numpy as np
import cv2 as cv

def affine_flip():
    src = cv.imread('soodal.jpeg')

    if src is None:
        print('Imeage load failed')
        return
    cv.imshow('src', src)

    for flip_code in [1, 0 , -1]:
        dst = cv.flip(src, flip_code)

        desc = 'flipcode: %d' %flip_code
        cv.putText(dst, desc, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0 ,0), 1, cv.LINE_AA)

        cv.imshow('dst', dst)
        cv.waitKey()
    cv.destroyAllWindows()

affine_flip()