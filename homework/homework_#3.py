import numpy as np
import cv2 as cv

old = -1 # 밝기 변화가 30이상으로 바뀔때와 전 프레임과 비교하기 위한 변수
inverse_check = False # 변화가 되었으면 True로 변환 초기값은 => False

video = cv.VideoCapture(1) # VideoCapture로 캠 화면 실행 => cv.CAP_DSHOW ( delay = 0 값으로 나오기 때문에 사용 x)

if not video.isOpened(): # 카메라가 열리지 않을때 예외 처리 구문
    print("Camer open failed")
    exit()

w = round(video.get(cv.CAP_PROP_FRAME_WIDTH)) # 출력되는 videoframe 넓이
h = round(video.get(cv.CAP_PROP_FRAME_HEIGHT)) # 출력되는 videoframe 높이

fourcc = cv.VideoWriter_fourcc(*'mp4v') # 동영상 파일 저장하기 위한 fourcc 문자 코드 설정

fps = video.get(cv.CAP_PROP_FPS) # 동영상 FPS 값을 확인하기 위해 CAP_PROP_FPS 사용

delay = round(100/fps) # 빠르게 재생되는 것을 방지하기 위해 초당 프레임 설정을 100

outputVideo = cv.VideoWriter('output.mp4', fourcc, fps, (w,h),0) # avi일때에는 동영상 저장이 안됨 노트북 문제인것 같음? -> mp4일떄에는 잘된다.
if not outputVideo.isOpened(): # 비디오 파일 저장이 안될때 예외처리
    print('File open failed')
    exit()

while True:

    ret, frame = video.read() # frame을 통해 Numpy array로 들어오게 된다.

    if not ret: # 예외처리
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # 영상화면을 회색으로 변경

    frame_mean = round(np.mean(frame)) # 평균 프레임을 구하기 위해 np.mean 사용

    # if -> 밝기변화가 30을 넘었을 때 inversed 되겠금 해주는 if 절
    if inverse_check or old != -1 and (frame_mean > old + 30 or frame_mean < old-30 ): # inversed_check / old = -1 이 아니라 평균 프레임이 old 변수 값에 의해 30이 넘었을 때
        inversed = ~gray # 색상 반전 사용
        inverse_check = True # inversed_check = True로 변경
        cv.imshow('output', inversed) # inversed 된 값 출력
        outputVideo.write(inversed) # inversed 된 값 video 저장

    # 아닐시에는 기존 gray 값 출력
    else:
        old = frame_mean
        outputVideo.write(gray)

        cv.imshow('gray',gray)


    if cv.waitKey(delay) == 27: # ESC 눌렀을 때 종료
        break

video.release()
cv.destroyAllWindows()
