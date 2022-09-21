import cv2 as cv

img = cv.imread('soodal.jpeg',cv.IMREAD_COLOR)

cartoon = cv.stylization(img, sigma_s = 100,sigma_r = 0.5)

cv.imshow('original', img)
cv.imshow('cartoon', cartoon)
cv.waitKey(0)
cv.destroyAllWindows()