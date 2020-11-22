import cv2 # importa OpenCV
import numpy as np #importa numpy
import random_color
x=140 # posição inicial x
y=180 # posição inicial y
altura=50 #dimenção do quadrado
counter=0 # contagem de frame
ponto=-20 # ponto do jogador
aux=0
def draw(frame):
    cv2.rectangle(frame, (10, 10), (120, 55), (80, 0, 80), cv2.FILLED)# desenha retângulo
    cv2.putText(frame,"p: "+str(ponto),(10,40),
                cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)# desenha texto

cap=cv2.VideoCapture(0) #Inicia webcam
fundo=cap.read()[1][y:y+altura,x:x+altura,] #captura primeiro fundo
while(cap.isOpened()): # repetir
    frame=cap.read()[1] # pega um quadro
    frame=cv2.flip(frame,180) # inverte quadro
    if counter>20: # atualiza fundo a cada 20 quadros
        fundo = frame[y:y + altura, x:x + altura,].copy()# atualiza fundo
        counter=0 # zera contador

    counter+=1 # incrementa contador

    rec=frame[y:y+altura,x:x+altura] # pega região embaixo do quadrado

    soma=np.sum(cv2.absdiff(rec,fundo)) # compara fundo com quadro atual
    print(soma)
    if soma>78000: # testa se tem movimento
        ponto+=1 # pontua jogadot
        x=np.random.randint(0,frame.shape[1]-altura) # cria nova coordenada x
        y=np.random.randint(0,frame.shape[0]-altura) # cria nova coordenada y
        fundo = frame[y:y + altura, x:x + altura, ].copy() # atualiza fundo
    frame[y:y+altura,x:x+altura,]=random_color.new_color(ponto) # desenha retângulo
    draw(frame) # desenha pontuação
    #cv2.rectangle(frame,(100,100),(150,150),(255,0,0),cv2.FILLED)
    cv2.imshow("janela",frame) # cria janela
    #if aux%10==0:
    #    cv2.imwrite(str(aux) + ".jpg", frame)
    aux+=1
    #cv2.imshow("fundo",fundo)
    k=cv2.waitKey(30) # aguarda um milissegundo
    if k==ord("q"): # se q for pressionado finaliza jogo
        break