import numpy as np
import cv2
img = np.zeros((200,200,3), np.uint8)
# desenhe aqui
cv2.line(img=img, #imagem
         pt1=(0,0), # ponto inicial
         pt2=(100,100), # ponto final
         color=(0,255,0), # cor BGR
         thickness=2, # largura da linha
         lineType=cv2.LINE_AA) # tipo de linha

cv2.rectangle(img=img, #imagem
         pt1=(0,0), # ponto inicial
         pt2=(100,100), # ponto final
         color=(0,255,0), # cor BGR
         thickness=2, # largura da linha
         lineType=cv2.LINE_AA) # tipo de linha

cv2.circle(img=img, # img
           center=(150,150), #centro (x,y)
           radius=20, # raio em px
           color=(0,0,255), #color vermelha BGR
           thickness=cv2.FILLED, # preencher
           lineType=cv2.LINE_AA) # tipo de linha

cv2.putText(img=img, # imagem
            text="OpenCV",# texto (não por acentos)
            org=(20,100),# ponto de origem (x,y)
            fontFace=cv2.FONT_HERSHEY_COMPLEX, # fonte
            fontScale=1.4,# escala
            color=(255,0,0),# color azul
            thickness=2, # largura da linh
            lineType=cv2.LINE_4, #Tipo de linha
            bottomLeftOrigin=False)# ponto de origem se True inverte eixo y
cv2.imshow("janela",img)
cv2.waitKey()
cv2.imwrite("saida.jpg",img)
cv2.destroyWindow()