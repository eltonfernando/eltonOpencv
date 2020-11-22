import cv2
img = cv2.imread("my_img.png")
cv2.imshow("Janela", img)
k=cv2.waitKey(0)

if k == ord("s"): # se s for pressionado salva a imagem
    cv2.imwrite("out.png", img)
cv2.destroyAllWindows()
