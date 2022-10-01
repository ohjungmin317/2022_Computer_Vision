# 마우스 이벤트 처리 
import cv2 as cv

def on_mouse(event, x, y, flags, param):
    global oldx, oldy # 밖에 있는 전역변수 oldx oldy를 불러온다.

    if event == cv.EVENT_LBUTTONDOWN: # 마우스의 왼쪽이 눌러지면 실행
        oldx, oldy = x,y
        print('EVENT_LBUTTONDOWN: %d, %d' %(x,y))

    elif event == cv.EVENT_LBUTTONUP: # 마우스를 손에서 뗏을때 실행
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    elif event == cv.EVENT_MOUSEMOVE: # 마우스가 손에서 움직일때 실행
        if flags & cv.EVENT_FLAG_LBUTTON: # 다른 키를 입력을 통해 작동이 되도록 실행하기 위해 &를 사용
            cv.line(img, (oldx, oldy), (x,y), (0,255,255),2) # 마우스를 통해 라인을 그랬을 노란색으로 설정
            cv.imshow('img',img) # img show에서 실행
            oldx,oldy = x,y # 그림을 그리고 좌표를 저장

img = cv.imread('soodal.jpeg')

if img is None:
    print('Image load failed!')
    exit()

cv.namedWindow('img')
cv.setMouseCallback('img', on_mouse)

cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()