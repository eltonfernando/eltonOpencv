import cv2
import numpy as np
#import pyautogui as teclado
UP='up'
#teclado.keyDown("down")
from time import time
#time.sleep(0.5)
#teclado.keyUp('down')

class FaceDetect():
    def __init__(self):
        self.face_detect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        print(self.face_detect.getOriginalWindowSize())
        self.cy=0
    def detect(self,img):
        cx=0
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.face_detect.detectMultiScale(gray,scaleFactor=1.1,
                                                minNeighbors=8,#distancia para considerar sobreposicao
                                                minSize=(25,25))# filtra retangulo menor 30x30
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0))
            cx=x+w//2
            self.cy=y+h//2
            cv2.circle(img,(cx,self.cy),2,(255,0,0))

        return cx,self.cy

class Kalman2DSort(object):
    def __init__(self, point_init,):
        """
        x: matriz 4x1 estado (x,y) velocidade em x e velocidade em y
        P: matriz 4x4 incerteza inicial
        u: matriz de aceleração
        F: matriz 4x4 funcão de estado
        H: matriz 2x4 função de medição
        R: matriz 2x2 incerteza de medição
        Q: matriz 4x4 incerteza do modelo
        I: matriz 4x4 identidade
        lastResult: matriz 2x1 guarda resuldado enterior
        :param point_init:list com coordenada [x,y]
        """

        self.inicio = time()
        self.x = np.array([[point_init[0]],[0.1],[point_init[1]],[0.1]])  # initial state (location and velocity)
        self.P = np.eye(4)   # initial uncertainty

        self.H = np.array([[1.0,0,0,0],
                           [0  ,0,1,0]]) # measurement function
        self.R = np.eye(2) * 0.0004  # incerteza do sensor
        self.Qv =np.array([[0.0,0,0,0],
                           [0,1.0,0,0],
                           [0,0,0,0],
                           [0,0,0,1.0]],dtype=np.float64)*1

        self.I = np.eye(4)  # identity matrix

    def correction(self, Z, flag=True):
        """
        y=Z-HK
        S=H*P*trans(H) +R
        K=P*trans(H)*inv(S)
        x=x+(k*y)
        P=(I-k*H)P
        :param Z: np.array[[x],[y]]
        :param flag: 0 quando não tem medição
        :return:Matrix 2x1 com coordenada (x,y)
        isso pode ser alterado para retorna velocidade
        estimada pelo filtro
        """
        if not flag:
            Z=np.dot(self.H,self.x)

        y = Z - (np.dot(self.H, self.x))
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        k = np.dot(self.P, np.dot(self.H.T, np.linalg.inv(S)))
        self.x = self.x + np.dot(k, y)
        #aux = self.I - np.dot(k, self.H)
        self.P = np.dot((self.I - np.dot(k, self.H)), self.P)
        #self.P = np.dot(np.dot(np.dot(aux, self.P), self.P), aux.T) + np.dot(np.dot(k, self.R), k.T)
        return np.asarray(self.x).reshape(-1) # # [x,vx,y,vy]

    def prediction(self):
        """
        Estima medida futura
        x'=FX + U
        P'=FPtrans(F) + Q
        :return:
        """
        delta = time() - self.inicio
        self.inicio = time()
        F = np.array([[1., delta, 0, 0],
                      [0, 1., 0, 0],
                      [0, 0, 1, delta],
                      [0, 0, 0, 1]])
        Q = np.dot(np.dot(F, self.Qv), F.T)
        self.x = np.dot(F, self.x)  # +self.u
        self.P = np.dot(F, np.dot(self.P, F.T)) + Q