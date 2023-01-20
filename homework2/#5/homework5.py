# https://velog.io/@dldndyd01/OpenCV-bitwiseand-or-xor-not-%EA%B8%B0%EB%8A%A5-%EC%A0%95%EB%A6%AC-RGB-Image - bitwise_not
# https://lucathree.github.io/python/day49-3/ - 원 윤곽선 검출 및 탐색 계층 구조

import cv2
import numpy as np

# 주사위 1,3,5 일때
img = cv2.imread("#5_dice1.png", cv2.IMREAD_COLOR)
# img = cv2.imread("#5_dice3.png", cv2.IMREAD_COLOR)
# img = cv2.imread("#5_dice5.png", cv2.IMREAD_COLOR)

if img is None: # 이미지가 없을때 예외처리
    print('Image load failed!')
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # 해당 사진을 grayscale 영상으로 변환

img_filter = cv2.bilateralFilter(gray,-1, 300, 6) # bilateralFilter을 이용하여 잡음 제거 및 원하는 개체만 검출 되기 위해 나머지 값 블러 처리
ret, binary = cv2.threshold(img_filter, 127, 255, cv2.THRESH_BINARY) # threshold 값 이용하여 출력되야 하는 거리 값 계산

# 주사위 6 검출할때 주석 해제
# img = cv2.imread("#5_dice6.png", cv2.IMREAD_COLOR)
#
# if img is None: # 이미지가 없을때 예외처리
#     print('Image load failed!')
#     exit()
#
# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#
# img_filter = cv2.bilateralFilter(gray, -1, 380, 7) # for dice number 6
# ret, binary = cv2.threshold(img_filter, 10, 255, cv2.THRESH_BINARY) # for dice number 6

# img_4 사진 일때 해당 주사위 눈 검출할 때 주석 해제
# img = cv2.imread("img_4.png", cv2.IMREAD_COLOR)
#
# if img is None: # 이미지가 없을때 예외처리
#     print('Image load failed!')
#     exit()
#
# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#
# img_filter = cv2.bilateralFilter(gray,-1, 250, 6) # for img number 4
# ret, binary = cv2.threshold(img_filter, 32, 255, cv2.THRESH_BINARY) # for img number 4

binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # 윤곽선 검출 -> RETR_TREE 이용하여 개체 검출하고 안에 있는 원 검출 할 수 있도록
circle_num = 0 # 원의 개수 초기화
count =[] # 원의 개수 list 값 초기화

for i in range(len(contours)):
    cv2.drawContours(img, [contours[i]], 0, (0, 0, 255), 3) # 윤곽선 검출이 되면 눈으로 볼 수 있도록 그리는 OpenCV 함수

    # 해당 개체 에서 -1 받거나 원을 검출하여 원 검출이 끝나는 지점 -1을 받을 때 원이라고 출력하고 원의 개수 + 1
    if hierarchy[0][i][2] == -1:
        if hierarchy[0][i][0] == -1:
            circle_num += 1
            count.append(circle_num)
            circle_num = 0
        else:
            circle_num += 1

    cv2.imshow('filter', img_filter) # 필터 값 확인하여 잡음이 얼마나 제거 되었는지 확인
    cv2.imshow('binary',binary) # 이진화 된 파일이 되어 개체만 잘 출력이 되었는지 확인
    cv2.imshow('output', img)  # 원본 이미지에 출력하여 원의 개수가 몇개인지 확인
    cv2.waitKey() # ESC 키를 눌러 개채 확인

print('number of circle', end=': ')

for i in count:
    print(i)

cv2.destroyAllWindows()

