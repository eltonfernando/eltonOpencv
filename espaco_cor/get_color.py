import cv2
import numpy as np
cv2.namedWindow("janela")
cap=cv2.VideoCapture("input02.mp4")
def mause(pos):
    pass
cv2.createTrackbar("H_min", "janela" , 0, 180,mause)
cv2.createTrackbar("S_min", "janela" , 0, 255,mause)
cv2.createTrackbar("V_min", "janela" , 0, 255,mause)
cv2.createTrackbar("H_max", "janela" , 0, 180,mause)
cv2.createTrackbar("S_max", "janela" , 0, 255,mause)
cv2.createTrackbar("V_max", "janela" , 0, 255,mause)
while(cap.isOpened()):
    ret,frame=cap.read()
    frame=cv2.resize(frame,(800,400))
    h_min = cv2.getTrackbarPos("H_min", 'janela')
    s_min = cv2.getTrackbarPos("S_min", 'janela')
    v_min = cv2.getTrackbarPos("V_min", 'janela')
    h_max = cv2.getTrackbarPos("H_max", 'janela')
    s_max = cv2.getTrackbarPos("S_max", 'janela')
    v_max = cv2.getTrackbarPos("V_max", 'janela')
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    maks=cv2.inRange(hsv,np.array([h_min,s_min,v_min]),np.array([h_max,s_max,v_max]))

    saida=cv2.bitwise_and(frame,frame,mask=maks)
    string = "H_min " + str(h_min)+" S_min "+str(s_min)+ " V_min "+str(v_min)
    string=string+" H_max " + str(h_max)+" S_max "+str(s_max)+ " V_max "+str(v_max)
    cv2.putText(saida, string, (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 0, 255))
    cv2.imshow("janela",saida)
    k = cv2.waitKey(180)
    if k ==ord("q"):
        break
