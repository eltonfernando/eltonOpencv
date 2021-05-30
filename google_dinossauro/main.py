
import numpy as np
import pyautogui as teclado
from threading import Thread
import time
import cv2
import core
from collections import deque
point=deque(maxlen=20)
cap=cv2.VideoCapture(0)
face_detecte=core.FaceDetect()
#kf=core.Kalman2DSort([0,0])

linha_auto=160
linha_baixo=240

counter_frame=0
cy=0
def chek_tecla():
    print("therd")
    pressed_up = False
    pressed_down = False
    global cy
    while True:
        if cy < linha_auto:
            if not pressed_up:
                teclado.keyDown('space')
                time.sleep(0.095)
                teclado.keyUp('space ')
                print("up")
                pressed_up = True
        else:
            pressed_up = False
            #pressed_down = False

thead=Thread(target=chek_tecla)
thead.start()
while True:

    ret, frame = cap.read()
    cv2.line(frame,(0,linha_auto),(frame.shape[1],linha_auto),(0,0,255))
    cv2.line(frame, (0, linha_baixo), (frame.shape[1], linha_baixo), (0, 0, 255))
    cx,cy=face_detecte.detect(frame)
    if cx!=0:
        point.append([cx, cy])
    if counter_frame<30:
        counter_frame+=1
        linha_baixo=cy+30
        linha_auto=cy-30
        face_detecte.cy=cy
        cv2.putText(frame,"calibrando",(cx+30,cy),cv2.FONT_HERSHEY_SIMPLEX,1,cv2.LINE_AA)

   #     cx,xv,cy,yv=kf.correction(np.array([[cx],[cy]]))
   #     kf.prediction()q
   # else:
    #    cx,xv,cy,yv=kf.correction(np.array([[cx], [cy]]),False)
   #     kf.prediction()


    for (x,y) in point:
        cv2.circle(frame,(x,y),2,(0,255,0))
    cv2.imshow("frame", frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        cap.release()
        break

thead.join()


if __name__=="__main__":
    pass
