import cv2
import numpy as np

src = cv2.imread("#4_dices.PNG", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
gray1 = cv2.bilateralFilter(gray,-1, 300, 6)
ret, binary = cv2.threshold(gray1, 140, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
circle_num = 0
count =[]

for i in range(len(contours)):
    cv2.drawContours(src, [contours[i]], 0, (255, 0, 0), 2)
    #cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    print(hierarchy) # 훈서 우리가 분석해봐야할거 같음 여기를

    if hierarchy[0][i][2] == -1:
        if hierarchy[0][i][0] == -1:
            circle_num += 1
            count.append(circle_num)
            circle_num = 0
        else:
            circle_num += 1

    cv2.imshow("src", src)
    cv2.waitKey(0)

count.sort()
print(count)
cv2.destroyAllWindows()