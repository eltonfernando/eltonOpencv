import cv2
import numpy as np
from draw import Rosto

cap =cv2.VideoCapture(1)
WIDTH=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
HEIGHT=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

mauser_point=(0,0)
box_raste=[]
def mauser_pose(event,x,y,flag,par):
    global mauser_point,box_raste
    mauser_point=(x,y)
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(box_raste) == 2:
            box_raste=[]
        if len(box_raste) == 1:
            box_raste.append((x, y))
        if len(box_raste)==0:
            box_raste.append((x,y))



rosto=Rosto(400,500)
rosto.start()
from Rastreador import MeidianFow
traing=MeidianFow()
while cap.isOpened():

    ret, frame=cap.read()
    x, y = mauser_point
    if len(box_raste)==1:
        traing.tracker=None
        cv2.rectangle(frame,box_raste[0],(x,y),(0,255,0),1)
    if len(box_raste)==2:
        cv2.rectangle(frame,box_raste[0],box_raste[1],(0,255,0),1)
        if traing.tracker is None:
            traing.start(frame,box_raste)
        else:
            ret=traing.predict(frame)
            if not ret is None:
                x,y,w,h=ret

    rosto.update(x,y)

    cv2.imshow("janela",frame)
    cv2.imshow("animation",rosto.get_rosto())
    cv2.setMouseCallback("janela", mauser_pose)
    k=cv2.waitKey(30)

    if k==ord("q"):
        break