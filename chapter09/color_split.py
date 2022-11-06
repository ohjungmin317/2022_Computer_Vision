import numpy as np
import cv2 as cv

def color_split():
    src = cv.imread('candies.png',cv.IMREAD_COLOR)

    if src is None:
        print('Image load failed')
        return

    bgr_planes = cv.split(src)

    cv.imshow('src',src)
    cv.imshow('B_plane',bgr_planes[0])
    cv.imshow('G_plane',bgr_planes[1])
    cv.imshow('R_plane',bgr_planes[2])
    cv.waitKey()
    cv.destroyAllWindows()

color_split()
