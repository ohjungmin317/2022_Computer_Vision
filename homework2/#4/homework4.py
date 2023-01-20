# https://jvvp.tistory.com/1126 - setLabel 함수 도형 검출기
# https://deep-learning-study.tistory.com/104 - 마스크 연산 ( 주사위에서 개체 따로 원 따로 검출하여서 mask 연산을 이용하여 합성 하여 남은 잡은 제거 및 원 검출 )
# https://bkshin.tistory.com/entry/OpenCV-19-%EB%AA%A8%ED%8F%B4%EB%A1%9C%EC%A7%80Morphology-%EC%97%B0%EC%82%B0-%EC%B9%A8%EC%8B%9D-%ED%8C%BD%EC%B0%BD-%EC%97%B4%EB%A6%BC-%EB%8B%AB%ED%9E%98-%EA%B7%B8%EB%A0%88%EB%94%94%EC%96%B8%ED%8A%B8-%ED%83%91%ED%96%87-%EB%B8%94%EB%9E%99%ED%96%87 - 모폴로지 연산

import numpy as np
import cv2 as cv
import math

global hsv

# 주사위의 개체 사각형을 검출하면서 그리는 함수
def setLabel_squre(img, pts):
    # 사각형 도형 좌표 받아오기
    (x, y, w, h) = cv.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h) # 꼭지점 사각형
    cv.rectangle(img, pt1, pt2, (255, 0, 0), 2)
    # cv.putText(img, label, pt1, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

def setLabel_circle(img, pts):
    # 원 도형 좌표 받아오기
    (x, y, w, h) = cv.boundingRect(pts)
    pt1 = (x, y+2)
    pt2 = (x + w+4, y + h+8) # 꼭지점 사각형
    cv.rectangle(img, pt1, pt2, (0, 255, 0), 2)
    # cv.putText(img, label, pt1, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


img = cv.imread('#4_dices.PNG', cv.IMREAD_COLOR) # 개체 검출을 위한 이미지 받아오기

if img is None: # 이미지가 없을때 예외처리
    print('Image load failed!')
    exit()

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #gray_scale로 변환

gradient = np.zeros((gray_img.shape[0], gray_img.shape[1])) #gray이미지에 대해 초기화

gradient = gradient.astype(np.uint8) # 해당 타입을 uint8로 변환


edge_dect = cv.Canny(gray_img, 50, 80) # Canny 검출기 이용하여 edge 검출

contours, _ = cv.findContours(edge_dect, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) # edge 검출 이용하여 윤곽선 찾기

# 도형에서 55 보다 작은 것은 원으로 검출 x -> 잡음 처리
for pts in contours:
    if cv.contourArea(pts) < 55:
        continue

    # 근사화
    approx = cv.approxPolyDP(pts, cv.arcLength(pts, True) * 0.02, True)

    vtc = len(approx) # 근사화 점 갯수 검출

    # 개체에서 원만 검출하는 연산
    lenth = cv.arcLength(pts, True)
    area = cv.contourArea(pts)
    circle_ratio = 4. * math.pi * area / (lenth * lenth)
    if circle_ratio > 0.85:
        for idx in pts[0]:
            cv.circle(gradient, (idx[0], idx[1]), 4, 255, -1, cv.LINE_AA)

cv.imshow('mask for circle', gradient)

# 마스크 처리 -> 사각형 개체 검출
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower = (7, 100, 0)
upper = (49, 255, 255)

mask = cv.inRange(hsv, lower, upper)
cv.imshow('mask for square', mask)

# CLOSE 연산하여 개체 중 어두운 연산을 효과적으로 제거
dst = cv.morphologyEx(mask, cv.MORPH_CLOSE, None)

gradient[dst > 0] = 255 # 마스크 연산 개체와 원 합성

cv.imshow('dice', gradient) # 우리가 원하는 주사위 개체 검출 - 잡음과 선 검출 없애고 순수 주사위만 검출

lines = cv.HoughLinesP(gradient, 1, math.pi / 180, 40, minLineLength=20, maxLineGap=5) # HoughLinesP 이용하여 선 검출
gradient_line = cv.cvtColor(gradient, cv.COLOR_GRAY2BGR)

if lines is not None: # 만약에 선이 아닐시에는 사각형 + 원으로 검출
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])
        pt2 = (lines[i][0][2], lines[i][0][3])
        cv.line(gradient_line, pt1, pt2, (255, 255, 255), 2, cv.LINE_AA)

gradient_dice = cv.cvtColor(gradient_line, cv.COLOR_BGR2GRAY)

contours, _ = cv.findContours(gradient_dice, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) # RETR_TREE 이용하여 개체안에는 자식 개체까지 검출

count_circle = [0] * 100
index = 0

for pts in contours: # 30이하는 사각형으로 검출 X -> 잡음 처리
    if cv.contourArea(pts) < 30:
        continue
    # 근사화
    approx = cv.approxPolyDP(pts, cv.arcLength(pts, True) * 0.02, True)
    vtc = len(approx) # 근사화 점의 개수

    if vtc == 4: # 점의 개수가 4개일때에는 사각형
        setLabel_squre(img, pts)
        index += 1 # 사각형 개수 1씩 증가

    else: # 사각형 아닐 때에는 원 검출
        lenth = cv.arcLength(pts, True)
        area = cv.contourArea(pts)
        circle_ratio = 4. * math.pi * area / (lenth * lenth)
        if circle_ratio > 0.87:
            setLabel_circle(img, pts)
            count_circle[index] += 1 # 원 검출 개수 1씩 증가하여 count list에 추가

count_circle.sort() # 원 개수 오름차순으로 정렬
print('number of circle ', end=': ')

for i in count_circle:
    if i != 0:
        print(i, end=' ')

cv.imshow('final_dice', gradient)
cv.imshow('output', img)
cv.waitKey()
cv.destroyAllWindows()