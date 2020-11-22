import cv2
import numpy as np
cap=cv2.VideoCapture("input02.mp4")#"http://10.0.0.104:4747/video")

# gravar saida processada
fourcc=cv2.VideoWriter_fourcc(*'mp4v')

im=cap.read()[1][:,520:-320,]
print(im.shape)
im=cv2.resize(im,(1080,1080))

h,w,_=im.shape
out=cv2.VideoWriter('saida.mp4', fourcc, 30,(w, h))

#define intervalos de cores
azul=[(93.0, 90 , 50),(130, 255.0, 254.6)]
laranja=[(0.0, 130.45, 150), (16, 200.0, 224.75)]
while(cap.isOpened()):
    img=cap.read()[1][100:-100,620:-420,] # le um frame
    img = cv2.resize(img,(1080,1080))
    hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # converte para escala HSV
    # cria mascara para cor azul
    mask_azul = cv2.inRange(hsv_img, np.array(azul[0]), np.array(azul[1]))
    mask_azul[0:100,0:200]=0
    # pega contorno dos objetos da mascara
    cnt_azul=cv2.findContours(mask_azul,
                              cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    # ordena por area e pega os dois maiores objetos
    cnt_azul=sorted(cnt_azul, key=cv2.contourArea, reverse=True)[:2]

    if cnt_azul: # testa se encontrou objeto azul
        for cont in cnt_azul: # pecorre contoros encontrados
            # pega centro e raio de um circo incrito do objeto
            (cx,cy),raio=cv2.minEnclosingCircle(cont)
            if raio <10:
                continue
            # escreve nome da cor
            cv2.putText(img,"Azul",(int(cx),int(cy)),
                    cv2.FONT_HERSHEY_TRIPLEX,1.2,(255,0,0),2)
            # Desenha circulo
            #cv2.circle(img,(int(cx),int(cy)),int(raio),(255,0,0),3)
            cv2.drawContours(img,[cont],0,(255,0,0),4)

    # repeto porcesso para cor laranja mais pegamos apena um objeto
    mask_laranja = cv2.inRange(hsv_img, np.array(laranja[0]), np.array(laranja[1]))
    cnt_laranja = cv2.findContours(mask_laranja,
                                   cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cnt_laranja = sorted(cnt_laranja, key=cv2.contourArea, reverse=True)[:1]

    if cnt_laranja:
        (cx, cy), raio = cv2.minEnclosingCircle(cnt_laranja[0])
        cv2.putText(img, "Laranja", (int(cx), int(cy)),
                    cv2.FONT_HERSHEY_TRIPLEX, 1.2, (28, 153, 206), 2)
        #cv2.circle(img, (int(cx), int(cy)), int(raio),(28, 153, 206),3)
        cv2.drawContours(img, cnt_laranja, 0, (28, 153, 206), 4)

    cv2.imshow("img",img) #atualiza janela
    k=cv2.waitKey(10) # aguarda
    out.write(img)
    if k==ord("q"): # finaliza de a tecla q for precionada
        break