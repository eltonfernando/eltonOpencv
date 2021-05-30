#!/usr/bin/python
# coding: utf-8
"""

    File name         : kalman2D,py
    File Description  : filtro de kalman
                      :
    Author            : Eng. Elton Fernandes dos Santos
    Date created      : 16/01/2020
    Version           : v1.0
    Python Version    : 3.6
Filtro de kalmam de duas dimensão, considera aceleração constante
e sem input de controle.
"""
import numpy as np
from time import time

class Kalman2D(object):
    H = np.matrix([[1.0, 0., 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0]])  # measurement function
    R = np.eye(2) * 0.00015  # incerteza do sensor
    I = np.eye(6)  # identity matrix
    Qa=np.array([[0.0,0,0,0,0,0],
                 [0  ,0,0,0,0,0],
                 [0  ,0,1,0,0,0],
                 [0  ,0,0,0,0,0],
                 [0  ,0,0,0,0,0],
                 [0  ,0,0,0,0,1]])*5.1
    def __init__(self,point_init):
        """
        x: matriz 6x1 estado (x,y) velocidade em x e velocidade em y
        P: matriz 6x6 incerteza inicial
        u: matriz de aceleração
        F: matriz 6x6 funcão de estado
        H: matriz 2x6 função de medição
        R: matriz 2x2 incerteza de medição
        Q: matriz 6x6 incerteza do modelo
        I: matriz 6x6 identidade
        lastResult: matriz 6x1 guarda resuldado enterior
        :param FPS: Taxa de amostragem
        """

        self.inicio=time()
        self.x = np.array([[point_init[0]],[0.1],[0.01], [point_init[1]],[0.1],[0.01]]) # initial state (location and velocity)
        self.P = np.eye(6) # initial uncertainty
        # self.u = np.array([[0.], [0.],[0.],[0.]])  # external motion


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
        if not flag:# com oclusao
            Z = np.dot(self.H,self.x)
        y = Z - (np.dot(self.H, self.x))
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        k = np.dot(self.P, np.dot(self.H.T, np.linalg.inv(S)))
        self.x = self.x + np.dot(k, y)
        #aux = self.I - np.dot(k, self.H)
        self.P = np.dot((self.I - np.dot(k, self.H)), self.P)
       # self.P = np.dot(np.dot(np.dot(aux, self.P), self.P), aux.T) + np.dot(np.dot(k, self.R), k.T)
        return np.asarray(self.x).reshape(-1) # [x,xv,xa,y,yv,va]
    def prediction(self):
        """
        Estima medida futura
        :return:
        """
        dt=time()-self.inicio
        self.inicio=time()
        F = np.array([[1.,dt,dt*dt/2,0, 0,     0],
                      [0, 1., dt,    0, 0,     0],
                      [0, 0,  1,     0, 0,     0],
                      [0, 0,  0,     1,dt, dt*dt/2],
                      [0, 0,  0,     0, 1,    dt],
                      [0, 0,  0,     0, 0,    1]])

        Q = np.dot(np.dot(F, self.Qa), F.T)
        self.x = np.dot(F, self.x)  # +self.u
        self.P = np.dot(F, np.dot(self.P, F.T)) + Q




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
        F = np.array([[1.,delta,0,0],
                      [0, 1., 0,0],
                      [0, 0, 1, delta],
                      [0, 0, 0, 1]])
        Q=np.dot(np.dot(F,self.Qv),F.T)
        self.x = np.dot(F, self.x)  # +self.u
        self.P = np.dot(F, np.dot(self.P, F.T)) + Q

class KalmanBoxSort(object):
    H = np.array([[1.0,0, 0, 0, 0, 0],
                  [0,  0, 1, 0, 0, 0],
                  [0,  0, 0, 0, 1, 0],
                  [0,  0, 0, 0, 0, 1]])  # measurement function
    R = np.eye(4) * 0.0004  # incerteza do sensor
    Qv = np.array([[0.0,0, 0, 0,  0, 0],
                   [0  ,1, 0, 0,  0, 0],
                   [0  ,0, 0, 0,  0, 0],
                   [0,  0, 0, 1,  0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0  ,0, 0, 0,0, 0]], dtype=np.float64) * 0.1
    def __init__(self, bbox):
        """
        x: matriz 6x1 estado (x,y,xw,yh) velocidade em x e velocidade em y
        P: matriz 6x6 incerteza inicial
        u: matriz de aceleração
        F: matriz 6x6 funcão de estado
        H: matriz 4x6 função de medição
        R: matriz 4x4 incerteza de medição
        Q: matriz 6x6 incerteza do modelo
        I: matriz 6x6 identidade
        lastResult: matriz 2x1 guarda resuldado enterior
        :param point_init:list com coordenada [x,y]
        """

        self.inicio = time()
        self.x = np.array([[bbox[0]],[0.1],[bbox[1]],[0.1],[bbox[2]],[bbox[3]]])  # initial state (location and velocity)
        self.P = np.eye(6)   # initial uncertainty

        self.I = np.eye(6)  # identity matrix

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
        aux=self.I-np.dot(k,self.H)
        #self.P = np.dot((self.I - np.dot(k, self.H)), self.P)
        self.P = np.dot(np.dot(np.dot(aux, self.P),self.P),aux.T) +np.dot(np.dot(k,self.R),k.T)
        return np.asarray(self.x).reshape(-1) # [x,y,vx,vy]

    def prediction(self):
        """
        Estima medida futura
        x'=FX + U
        P'=FPtrans(F) + Q
        :return:
        """
        dt = time() - self.inicio
        self.inicio = time()
        F = np.array([[1.,dt,0,0 ,0,0],
                      [0 ,1 ,0,0 ,0,0],
                      [0 ,0 ,1,dt,0,0],
                      [0 ,0 ,0,1 ,0,0],
                      [0 ,dt,0,0 ,1,0],
                      [0 ,0 ,0,dt,0,1]])
        Q=np.dot(np.dot(F,self.Qv),F.T)
        self.x = np.dot(F, self.x)  # +self.u
        self.P = np.dot(F, np.dot(self.P, F.T)) + Q


