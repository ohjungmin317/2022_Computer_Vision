import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def calcGrayHist(src):
    channels = [0]
    histSize = [256]
    histRange = [0, 256]

    hist = cv.calcHist([src], channels, None, histSize, histRange)

    return hist


def getGrayHistImage(hist):
    _, histMax, _, _ = cv.minMaxLoc(hist)

    imgHist = np.ones((100, 256), np.uint8) * 255
    for x in range(imgHist.shape[1]):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv.line(imgHist, pt1, pt2, 0)

    return imgHist

# cv.imshow('src',src)
# cv.waitKey()
#
# plt.plot(hist)
# plt.show()
#
# cv.destroyAllWindows()

def histgoram_equalization():
    src = cv.imread('soodal.jpeg',cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    dst = cv.equalizeHist(src)

    cv.imshow('src',src)
    cv.imshow('srcHist',getGrayHistImage(calcGrayHist(src)))

    cv.imshow('dst',dst)
    cv.imshow('dstHist',getGrayHistImage(calcGrayHist(dst)))

    cv.waitKey()
    cv.destroyAllWindows()

histgoram_equalization()