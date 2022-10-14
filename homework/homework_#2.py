import numpy as np
import cv2 as cv

def saturated(value): # 포화 연산 수행 하는 함수
    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value


def contrast(): # 명암 조절
    img = cv.imread('sample.bmp',cv.IMREAD_GRAYSCALE) # 이미지를 회색조로 불러오는 구문

    img_mean = round(np.mean(img)) # 이미지의 평균 밝기 구하기

    if img is None: # 이미지가 열리지 않을 때 예외처리
        print('Image load failed')
        return

    s = 2.0 # 계수 = 2.0으로 선언

    dst = np.empty(img.shape, img.dtype) # 포화 연산 수행 및 반복하여 명암비 조절 단 0보다 작을 시에는 = 0 / 255보다 클때에는 255
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            dst[y, x] = saturated(img[y,x] +(img[y,x]-img_mean) * s)

    cv.imshow('sample',img) # 원래 이미지 출력 ( 비교용 )
    cv.imshow('contrast',dst) # 출력용 이미지 출력 ( 출력용 )
    cv.imwrite('contrast.jpg',dst) # 출력용 이미지 저장
    cv.waitKey()
    cv.destroyAllWindows()

contrast()


