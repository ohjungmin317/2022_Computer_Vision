# https://deep-learning-study.tistory.com/213 - 과제 1번 참고한 site

import numpy as np
import cv2 as cv

img = cv.imread('dice1.PNG', 0) # 이미지를 읽어옴
# img = cv.imread('dice2.PNG', 0)
# img = cv.imread('dice3.PNG', 0)
# img = cv.imread('dice4.PNG', 0)
# img = cv.imread('dice5.PNG', 0)
# img = cv.imread('dice6.PNG', 0)

if img is None: # 이미지가 없을때 예외처리
    print('Image load failed!')
    exit()

img = cv.bilateralFilter(img,-1, 300, 3) # 사진에 대한 잡음 처리 위한 필터
cvt_img = cv.cvtColor(img,cv.COLOR_GRAY2BGR) # 이미지를 grayscale로 변경하기

circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,param1=100,param2=30,minRadius=0,maxRadius=0) # 원 검출을 위해 OpenCV에서 제공해주는 HoughCircles 사용

circles = np.uint16(np.around(circles)) # 원 값에 대한 소숫값은 반올림

for i in circles[0,:]:
    cv.circle(cvt_img,(i[0],i[1]),i[2],(0,255,0),2) # 원을 검출하게 되면 해당 원에 대해 원 둘레 검출
    # cv.circle(cvt_img,(i[0],i[1]),2,(0,0,255),3) # 원을 검출하게 되면 해당 원 중심점 검출

cv.imshow('filter',img) # 잡음처리된 원을 검출
cv.imshow('output',cvt_img) # 결과 이미지 검출
print('check for list', circles) # 해당 사진에 대해 원 검출한 배열 값
print('number of circle:',len(circles[0])) # 해당 사진에 원이 몇개 있는 확인해주는 검출용
cv.waitKey(0)
cv.destroyAllWindows()
