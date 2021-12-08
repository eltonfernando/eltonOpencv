import cv2
import numpy as np
from draw import Rosto

cap =cv2.VideoCapture(1)
WIDTH=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
HEIGHT=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(WIDTH,HEIGHT)
mauser_point=(0,0)
def mauser_pose(event,x,y,flag,par):
    global mauser_point
    mauser_point=(x,y)

rosto=Rosto(400,400)
rosto.start()

while cap.isOpened():

    ret, frame=cap.read()

    x,y=mauser_point
    rosto.update(x,y)

    cv2.imshow("janela",frame)
    cv2.imshow("animation",rosto.get_rosto())
    cv2.setMouseCallback("animation", mauser_pose)
    k=cv2.waitKey(30)

    if k==ord("q"):
        break