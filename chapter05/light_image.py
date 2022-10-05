import numpy as np
import cv2 as cv

def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value

def light_image():
    src = cv.imread('soodal.jpeg',cv.IMREAD_GRAYSCALE)

    if src is None:
        print("Imeage load failed")
        return

    dst = np.empty(src.shape, dtype=src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y,x] = saturated(src[y, x] + 100)

    cv.imshow('img',src)
    cv.imshow('img2',dst)
    cv.waitKey()
    cv.destroyAllWindows()

light_image()