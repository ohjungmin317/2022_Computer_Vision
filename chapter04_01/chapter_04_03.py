import numpy as np
import cv2 as cv

img = np.full((400, 400, 3), 255, np.uint8)

cv.rectangle(img, (50,50), (150, 100), (0,0,255), 2)
cv.rectangle(img, (50,50), (150, 100), (0,0,255), -1)

cv.circle(img, (300, 120), 30, (255,255,0), -1, cv.LINE_AA)
cv.circle(img, (300, 120), 60, (255,0,0), 3, cv.LINE_AA)

cv.ellipse(img, (120, 300), (60, 30), 20, 0 , 270, (255,255,0), cv.FILLED, cv.LINE_AA)
cv.ellipse(img, (120, 300), (100, 50), 20, 0 , 360, (0,255,0), 2 , cv.LINE_AA)

pts = np.array([[250, 250], [300, 250], [300, 300], [ 350, 300], [350, 350], [250, 350]])
cv.polylines(img,[pts],True, (255,0,255), 2)

cv.imshow("img",img)
cv.waitKey()
cv.destroyAllWindows()
