#https://lucathree.github.io/python/day49-3/ - 원 윤곽선 검출 및 탐색 계층 구조

import cv2 as cv
import numpy as np

# 원하는 해당 이미지를 주석 처리 해제 해준다.
img = cv.imread("dices.PNG", cv.IMREAD_COLOR) # 개체 검출을 위한 이미지 load
# img = cv.imread("dices2.PNG", cv.IMREAD_COLOR)
# img = cv.imread("dices3.PNG", cv.IMREAD_COLOR)



if img is None: # 이미지가 없을때 예외처리
    print('Image load failed!')
    exit()

cvt_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY) #gray scale로 이미지 변환
ret, binary = cv.threshold(cvt_gray, 127, 255, cv.THRESH_BINARY) # 이진화 값으로 변환 [ threshold보다 크면 value이고 아니면 0으로 바꾸어준다. ]
binary = cv.bitwise_not(binary)

contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) # 주사위 객체 외곽선 먼저 검출 후 안에 있는 원의 외곽선을 개수를 검출하기 위해 RETR_TREE 사용
circle_num = 0
count =[] # 주사위 원 개수가 담겨져 있는 list

for i in range(len(contours)): # 외곽선을 검출하는 for문
    cv.drawContours(img, [contours[i]], 0, (0, 255, 0), 2) # 이미지에서 외곽선을 확인하기 위한 Opencv 함수
    cv.putText(img, str(i), tuple(contours[i][0][0]), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1) # 해당 외곽선 마다 번호를 붙히기 위한 Opencv putText 사용

    if hierarchy[0][i][2] == -1: # 2번째 전체 주사위 개체에서 -1를 만나게 되면 주사위 하나의 개체가 끝나기 때문에 circle_num count를 한개 증가
        if hierarchy[0][i][0] == -1: # 0번째 : 원의 개수를 검출하고 난 후 다음 개체를 검출할때 마지막 -1를 출력함.
            circle_num += 1 # 즉 , 전체 주사위 개체에서 -1 해당 주사위 개체에서 원 개수가 마지막이면 해당 개수를 count list에 append
            count.append(circle_num) # count list에 추가
            circle_num = 0 # 다시 초기화
        else:
            circle_num += 1 # 아닌 경우에는 그냥 circle 개수 한개 증가

    cv.imshow('cvt_gray', cvt_gray)
    cv.imshow('binary', binary)
    cv.imshow('output', img)
    cv.waitKey(0) #ESC 눌러서 주사위 개체와 원 개수 검출할 수 있도록 함. -> 해당 개체가 완료할때까지 esc 눌러야 한다.

count.sort() # append 된 숫자를 오름차순으로 출력
print('sort of dice circle count', end=': ')
for i in count:
    print(i, end='  ')
print(' ')
print(hierarchy) # 위치를 확인하기 위한 list 출력
cv.destroyAllWindows()
