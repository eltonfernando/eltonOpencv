import time

from filter.kalman import Kalman2DSort as filter
from filter.kalman import Kalman2D
from collections import deque
import numpy as np
import cv2

mause_points=deque(maxlen=120)
kf_sorted_point=deque(maxlen=120)
kf_point=deque(maxlen=120)
kf_sorted=filter([1, 1])
kf=Kalman2D([1,1])

count_oculsao=0
def mause_point(event,x,y,flags,param):
    global mause_points
    global kf_sorted
    global kf

    global count_oculsao
    flag = True
    cx,cy=x+np.random.randint(8),y+np.random.randint(8)
    z=np.array([[cx],[cy]])
    iniico=time.time()
    if count_oculsao>10:
        count_oculsao-=1
        flag=False
        print("olcusao")
    else:
        flag=True
        print("sem oclusao")
        count_oculsao+=1
    if x<200:
        flag=False
        print("oclucao 2")
    inicio = time.time()
    xn,vx,yn,vy=kf_sorted.correction(z,flag)
    kf_sorted.prediction()
    print(f' sorted {time.time()-iniico}')
    kf_sorted_point.append([int(xn), int(yn)])
    inicio=time.time()
    xn,xv,xa,yn,yv,ya=kf.correction(z,flag)
    kf.prediction()
    print(f' kf {time.time() - iniico}')
    kf_point.append([int(xn), int(yn)])
    mause_points.append([cx,cy])
cv2.namedWindow('image')
cv2.setMouseCallback('image',mause_point)


while True:
    img=np.ones((900,900,3))*255
    img[:,200:201]=(0,0,0)
    for (x,y),(xn,yn),(xn2,yn2) in zip(mause_points, kf_sorted_point, kf_point):
        cv2.circle(img,(x,y),2,(255,0,0),cv2.FILLED)
        cv2.circle(img,(xn,yn),2,(0,0,255),cv2.FILLED)
        cv2.circle(img,(xn2,yn2),2,(0,255,0),cv2.FILLED)

    cv2.imshow("image",img)
    k=cv2.waitKey(60)
    if k==ord("q"):
        break