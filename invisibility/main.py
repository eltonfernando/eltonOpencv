import cv2

import numpy as np
cap=cv2.VideoCapture("input.mp4")
cap_fundo=cv2.VideoCapture("fundo.mp4")
mean_fundo=[]
# calcula mediana de de 10 frame
#salvando fundo

for i in range(10):
    fundo=cap_fundo.read()[1]
    mean_fundo.append(fundo)

fundo = np.median(np.array(mean_fundo),axis=0)
fundo=fundo.astype(np.uint8)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
h, w, _ =fundo.shape
out = cv2.VideoWriter('s.mp4', fourcc, 30, (h, h))


while(cap.isOpened()):

    ret,frame=cap.read()
    if not ret:
        break
    print(frame.shape)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([30, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([120, 120, 70])
    upper_red = np.array([180, 255, 255])

    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    mask2 = cv2.bitwise_not(mask1)
    cv2.imwrite("maks1.jpg",mask1)
    cv2.imwrite("maks2.jpg", mask2)

    res1 = cv2.bitwise_and(frame, frame, mask=mask2)

    res2 = cv2.bitwise_and(fundo, fundo, mask=mask1)

    cv2.imwrite("res1.jpg", res1)
    cv2.imwrite("res2.jpg", res2)
    saida = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("janela", saida)
    k = cv2.waitKey(3)
    #out.write(frame)
    if k == ord("q"):
        break

cv2.destroyAllWindows()