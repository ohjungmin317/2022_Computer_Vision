import cv2 as cv

def mask_setTo():
    src = cv.imread('soodal.jpeg',cv.IMREAD_COLOR)
    mask = cv.imread('mask_smile.bmp', cv.IMREAD_GRAYSCALE)

    if src is None or mask is None:
        print('Image load failed')
        return

    src[mask > 0] = (0, 255, 255)

    cv.imshow('src',src)
    cv.imshow('mask',mask)
    cv.waitKey()
    cv.destroyAllWindows()
