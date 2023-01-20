import numpy as np
import cv2 as cv
import math


def setLabel(img, pts, label):
    (x, y, w, h) = cv.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv.putText(img, label, pt1, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


img = cv.imread('#4_dices.PNG', cv.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    exit()

dst1 = cv.GaussianBlur(img,(5,5),9)
cv.imshow('point', dst1)

edge = cv.Canny(dst1, 30, 100)
cv.imshow('point1', edge)

lines = cv.HoughLinesP(edge, 1, math.pi / 90, 30, minLineLength=0, maxLineGap=15)
edge = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)
if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])
        pt2 = (lines[i][0][2], lines[i][0][3])
        cv.line(edge, pt1, pt2, (255, 255, 255), 2, cv.LINE_AA)
cv.imshow('point2', edge)
edge = cv.cvtColor(edge, cv.COLOR_BGR2GRAY)
cv.imshow('point3', edge)

contours, _ = cv.findContours(edge, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
count = [0] * 100
index = 0

for pts in contours:
    if cv.contourArea(pts) < 30:
        continue

    approx = cv.approxPolyDP(pts, cv.arcLength(pts, True) * 0.02, True)
    vtc = len(approx)

    if vtc == 4:
        setLabel(img, pts, 'RECT')
        index += 1
    else:
        lenth = cv.arcLength(pts, True)
        area = cv.contourArea(pts)
        ratio = 4. * math.pi * area / (lenth * lenth)
        if ratio > 0.75:
            setLabel(img, pts, 'CIR')
            count[index] += 1

count.sort()
for i in count:
    if i != 0:
        print(math.ceil(i / 2))

cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()