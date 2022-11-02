import cv2 as cv

img = cv.imread('cat.bmp', cv.IMREAD_GRAYSCALE)
# img = ~img
# img[:int(img.shape[1] / 2), :] = ~img[:int(img.shape[1]/2),:]
img[img.shape[0]//2:,:] = ~img[img.shape[0]//2:,:]
# print (img.shape)
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()