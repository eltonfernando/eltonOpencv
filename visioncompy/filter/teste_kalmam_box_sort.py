import time


from filter.kalman import KalmanBoxSort
from collections import deque
import numpy as np
import cv2

mause_points=deque(maxlen=120)
kf_point=deque(maxlen=120)
box=deque(maxlen=120)
kf=KalmanBoxSort([1,1,20,80])

count_oculsao=0
def mause_point(event,x,y,flags,param):
    global mause_points
    global kf_sorted
    global kf

    global count_oculsao
    flag = True
    cx,cy=x+np.random.randint(8),y+np.random.randint(8)
    mw,mh=20+x+np.random.randint(4),80+y+np.random.randint(8)
    z=np.array([[cx],[cy],[mw],[mh]])
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

    xn,vx,yn,vy,w,h=kf.correction(z,flag)
    kf.prediction()

    print(f' kf {time.time() - iniico}')
    box.append([int(w),int(h)])
    kf_point.append([int(xn), int(yn)])


    mause_points.append([cx, cy])
cv2.namedWindow('image')
cv2.setMouseCallback('image',mause_point)


while True:
    img=np.ones((900,900,3))*255
    img[:,200:201]=(0,0,0)
    for (x,y),(xn,yn),(w,h) in zip(mause_points,kf_point,box):
        cv2.circle(img,(x,y),2,(255,0,0),cv2.FILLED)
        cv2.circle(img,(xn,yn),2,(0,0,255),cv2.FILLED)
        cv2.circle(img,(w,h),2,(0,255,0),cv2.FILLED)
        cv2.rectangle(img,(xn,yn),(w,h),(0,0,0),1)
    cv2.imshow("image",img)
    k=cv2.waitKey(60)
    if k==ord("q"):
        break