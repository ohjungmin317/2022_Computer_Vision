import numpy as np
import cv2 as cv


def camera_in():
    cap = cv.VideoCapture(1,cv.CAP_DSHOW)

    if not cap.isOpened():
        print("Camera open failed!")
        return

    print('Frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
    print('Frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        inversed = ~frame

        cv.imshow('frame', frame)
        cv.imshow('inversed', inversed)

        if cv.waitKey(10) == 27:
            break

    cv.destroyAllWindows()

if __name__ == '__main__':
    camera_in()


# cap = cv.VideoCapture('soodal.mp4')
# if not cap.isOpened():
#     print("Video open failed")
#     exit()
# print('Frame width:',int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
# print('Frame height:',int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
# print('Frame count:',int(cap.get(cv.CAP_PROP_FRAME_COUNT)))
#
# fps = cap.get(cv.CAP_PROP_FPS)
# print('FPS:',fps)
# delay = round(1000 / fps)
#
# while True:
#     ret, frame = cap.read()
#
#     if not ret:
#         break
#
#     inversed = ~frame
#
#     cv.imshow('frame',frame)
#     cv.imshow('inversed',inversed)
#
#     if cv.waitKey(delay) == 27:
#         break
# cv.destroyAllWindows()