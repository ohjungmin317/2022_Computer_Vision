# https://jvvp.tistory.com/1126 - setLabel 함수 도형 검출기

# 주사위 색상은 밝은 색 주사위 눈의 색상은 어두운색이고 배경은 어두운 배경
import numpy as np
import cv2 as cv
import math

img = cv.imread('dark_dice.png')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

if img is None:
    print('Image load failed!')
    exit()


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
    pt1 = (x, y+1)
    pt2 = (x + w+1, y + h+2) # 꼭지점 사각형
    cv.rectangle(img, pt1, pt2, (0, 255, 0), 2)
    # cv.putText(img, label, pt1, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


img_filter = cv.bilateralFilter(gray_img, -1, 150, 5) # 사진 잡음 처리
cv.imshow('img_filter', img_filter)

dect_edge = cv.Canny(img_filter, 35, 100) # canny 함수 이용하여 edge 검출
cv.imshow('dect_edge', dect_edge)

lines = cv.HoughLinesP(dect_edge, 1, math.pi / 90, 30, minLineLength=0, maxLineGap=15) # HoughLinesP 이용하여 선 검출
edge = cv.cvtColor(dect_edge, cv.COLOR_GRAY2BGR) # graysacle로 변환

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])
        pt2 = (lines[i][0][2], lines[i][0][3])
        cv.line(edge, pt1, pt2, (255, 255, 255), 2, cv.LINE_AA) # 해당 라인을 좀 더 진하게

cv.imshow('binary', edge)

edge = cv.cvtColor(edge, cv.COLOR_BGR2GRAY)

cv.imshow('binary_edge', edge)

contours, _ = cv.findContours(edge, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) # 해당 라인을 이용하여 윤곽선 검출
count_circle = [0] * 100
index = 0

# 외곽선 좌표 받아오기
for pts in contours:
    if cv.contourArea(pts) < 30: # 30이상 넘어가면 검출 x -> 노이즈 제거 너무 작으면 무시
        continue

    # 근사화
    approx = cv.approxPolyDP(pts, cv.arcLength(pts, True) * 0.03, True)
    vtc = len(approx) # 근사화 결과 점 갯수 검출

    if vtc == 4: # 근사화 한 점의 개수가 4개이면 사각형으로 검출
        setLabel_squre(img, pts)
        index += 1

    else: # 근사화 한 점의 개수가 4가 아닌 다른 것은 원으로 검출
        lenth = cv.arcLength(pts, True)
        area = cv.contourArea(pts)
        ratio = 4. * math.pi * area / (lenth * lenth)
        if ratio > 0.75:
            setLabel_circle(img, pts)
            count_circle[index] += 1 # 개체 안에 원이면 count 값 증가

count_circle.sort() # count 값 오름차순으로 정렬

print('number of circle ', end= ': ')

for i in count_circle: # 주사위 눈의 개수 출력 오름차순으로
    if i != 0:
        print(math.ceil(i / 2), end=' ')

cv.imshow('filter',img_filter)
cv.imshow('edge',edge)
cv.imshow('output', img)
cv.waitKey()
cv.destroyAllWindows()