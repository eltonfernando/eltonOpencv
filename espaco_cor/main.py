import cv2

img=cv2.imread("img.jpg")
img=img[1250:-900,500:-900]
print(img.shape)
img=cv2.resize(img,None,None,0.2,0.2)
HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
saida=cv2.hconcat((img,HSV))
cv2.imwrite("img2.jpg",img)
cv2.imshow("RBG",cv2.resize(img,(100,100)))
cv2.imwrite("saida.jpg",saida)
cv2.imshow("HSV",saida)


#cv2.imshow("y",Y)

cv2.waitKey()
