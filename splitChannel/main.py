import cv2
img = cv2.imread("logo.png")
b,g,r = cv2.split(img)

# 0.5ms mais rápido
np_r = img[:,:,2]
np_g = img[:,:,1]
np_b = img[:,:,0]

g[:,0:3]=255 #pinta as 3 primeira coluna de branco
r[:,0:3]=255 #pinta as 3 primeira coluna de branco


print(b)
saida=cv2.hconcat((b,g,r))# Coloca lado a lado os canais

cv2.imshow("Input",img)
cv2.imshow("R",r)
cv2.imshow("G",g)
cv2.imshow("B",b)

cv2.imwrite('saida.png',saida)
cv2.waitKey()
