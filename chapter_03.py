import cv2 as cv
import numpy as np

# (1) OpenCV 버전 확인
# print("Hello OpenCV", cv.__version__)

# (2) OpenCV 이미지 불러오기
# img = cv.imread('soodal.jpeg')
#
# if img is None:
#     print('Image load failed!')
#     exit()
# cv.imshow('image', img)
# cv.waitKey()

# (3) 이미지 타입 확인하기

# def func1():
#     img = cv.imread('soodal.jpeg',cv.IMREAD_GRAYSCALE)
#
#     if img is None:
#         print('Image load failed')
#         return
#
#     print('type(img):', type(img))
#     print('img.shape:',img.shape)
#
#     if len(img.shape) == 2:
#         print('img is a grayscale image')
#     elif len(img.shape) == 3:
#         print('img is a truecolor image')
#
#     cv.imshow('img',img)
#     cv.waitKey()
#     cv.destroyAllWindows()
#
# func1()

# (4) 행렬의 복사 - copy() 연산 사용

# def fun2():
#     img = cv.imread('soodal.jpeg')
#
#     img1 = img
#     img2 = img.copy()
#
#     img[:, :] = (0, 255, 255) # yellow color
#
#     cv.imshow('img', img)
#     cv.imshow('img1', img1)
#     cv.imshow('img2', img2)
#     cv.waitKey()
#     cv.destroyAllWindows()
#
# fun2()

# (5) 부분 행렬 추출

# def fun3():
#     img = cv.imread('soodal.jpeg',cv.IMREAD_GRAYSCALE)
#
#     img1 = img[200:400, 200:400]
#     img2 = img[200:400, 200:400].copy()
#
#     img1 += 20
#
#     cv.imshow('img',img)
#     cv.imshow('img1', img1)
#     cv.imshow('img2', img2)
#     cv.waitKey()
#     cv.destroyAllWindows()
#
# fun3()

# (6) 부분행렬 추출 후 반전
def fun4():
    img = cv.imread('soodal.jpeg')

    img1 = img[100:400, 100:400]
    img2 = img[100:400, 100:400].copy()

    out = img1.copy()
    out = 255 - out

    img1 += 20

    cv.imshow('img',img)
    # cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img1',out)
    cv.waitKey()
    cv.destroyAllWindows()

fun4()

