import cv2
img_BGR=cv2.imread("img.png")
img_hsv=cv2.cvtColor(img_BGR,cv2.COLOR_BGR2HSV)

cv2.imshow("janela",img_BGR)
cv2.imshow("hsv",img_hsv)
cv2.waitKey()
cv2.imwrite("hsv.png",img_hsv)