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
Este filtro foi implementado baseado na equação MRUV em X Y
e modelagem de espaço de estado
Filtro de kalaman é um modelo linear por isso não é
considerado a parte de aceleração.

Como Calibar:
Auterar  em __int__
Q: quanto menor o valor de Q mais confiavel é o modelo
R: quanto menor o valor de R mais confiavel é a medição
vale o mesmo para Q2 e R2 em que nesse caso R2>R e Q>Q2

Como usar
estancia a class
FK=Kaman()
verificar se  existe dados do sensor valido
se True: #sem oclusao
result= FK.correction(medida)
se false #com oclusao
result= FK.correction(medida,0)
FK.prediction()

"""
import numpy as np
from time import time
from numba import jit, void, int_, double,farray

@jit
class Kalman(object):
    #@void(int_,list)
    def __init__(self,point_init):
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
        :param FPS: Taxa de amostragem
        """

        self.inicio=time()
        self.x = np.array([[point_init[0]],[0],[0], [point_init[1]],[0.],[0]]) # initial state (location and velocity)
        self.P = np.eye(6)  # initial uncertainty

        # self.u = np.array([[0.], [0.],[0.],[0.]])  # external motion
        self.H = np.matrix([[1.0, 0.,0,0,0,0],
                           [0,0,0,1,0,0]]) # measurement function

        print(np.dot(self.H,self.x))
        self.R = np.eye(2) * 0.0001  # incerteza do sensor

        self.I = np.eye(6)  # identity matrix
        self.lastResult = self.x
        self.flag = 1

    def correction(self, Z, flag=1):
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
            Z = self.lastResult
        y = Z - (np.dot(self.H, self.x))
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        k = np.dot(self.P, np.dot(self.H.T, np.linalg.inv(S)))
        self.x = self.x + np.dot(k, y)
        self.P = np.dot((self.I - np.dot(k, self.H)), self.P)
        return np.asarray(self.x).reshape(-1) # [x,y,vx,vy]
    #@void()
    def prediction(self):
        """
        Estima medida futura
        x'=FX + U
        P'=FPtrans(F) + Q
        :return:
        """
        dt=time()-self.inicio
        if dt>0.2:
            dt=0.2
        self.inicio=time()
        F = np.array([[1.,dt,dt*dt/2,0, 0,     0],
                      [0, 1., dt,    0, 0,     0],
                      [0, 0,  1,     0, 0,     0],
                      [0, 0,  0,     1,dt, dt*dt/2],
                      [0, 0,  0,     0, 1,    dt],
                      [0, 0,  0,     0, 0,    1]])
        Q=np.array([[dt**4/4,dt**3/2,dt*dt/2,0,0      ,0],
                    [dt**3/2,dt*dt  ,dt,0     ,0      ,0],
                    [dt*dt/2,dt     ,1 ,0      ,0      ,0],
                    [0      ,0      ,0 ,dt**4/4,dt**3/2,dt*dt/2],
                    [0      ,0      ,0 ,dt**3/2,dt*dt  ,dt],
                    [0      ,0      ,0 ,dt*dt/2,dt     ,1]])

        self.x = np.dot(F, self.x)  # +self.u
        self.P = np.dot(F, np.dot(self.P, F.T)) + Q

        self.lastResult = self.x

