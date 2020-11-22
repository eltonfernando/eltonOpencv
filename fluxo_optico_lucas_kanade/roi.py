import cv2
import numpy as np
img=cv2.imread("image-016.jpeg")[:-300,:,]
roi=img[455:475,710:730,].copy()#retanguno
roi=img[432:452,710:730,].copy()
cv2.imwrite("roi.png",roi)
print(roi.shape)
cv2.imshow("roi",roi)
#roi=(0,0,0)

cv2.imshow("janela",img)
cv2.waitKey(0)