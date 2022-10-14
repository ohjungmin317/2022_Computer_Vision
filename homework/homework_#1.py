import numpy as np
import cv2 as cv

def fun():
    img = cv.imread('sample.bmp',cv.IMREAD_GRAYSCALE) # 이미지를 grayscale로 불러옴

    if img is None: # 이미지 파일이 열리지 않을 때 예외처리
        print('Image load failed')
        return

    img_mean = np.mean(img) # 이미지의 평균밝기 구하기

    dst = np.where(img < img_mean, 0, img) # 평균 밝기 보다 어두운 것은 픽셀을 0으로 바꾸기 where 사용

    desc = "20180775_Oh Jung Min"
    cv.putText(dst, desc, (20, 30), cv.FONT_HERSHEY_SIMPLEX,0.5,255,1,cv.LINE_AA)

    cv.imshow('sample',img) # 본 이미지 출력 ( 비교용 )
    cv.imshow('output',dst) # 평균 밝기 보다 어두운 픽셀을 0으로 바꾼 이미지 출력 ( 출력용 )
    cv.imwrite('output.jpg',dst) # 해당 이미지 저장
    cv.waitKey()
    cv.destroyAllWindows()

fun()
