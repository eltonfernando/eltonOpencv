"""
autor: Elton Fernandes dos santos

"""
import numpy as np
class Draw():
    def __init__(self,axi):
        self.ax1=axi
        self.x0=0
        self.y0=0
        self.grid=None
    def center(self):
        xc=0
        yc=0
        return xc,yc
    def rect(self,x0,y0,w,h):
        x = np.array([x0, x0 + w, x0 + w, x0, x0])
        y = np.array([y0, y0, y0 + h, y0 + h, y0])
        self.ax1.plot(x,y,color='b')
    def mat_grid(self,x0,y0,w,h,valor):
        """
        desenha uma grade para uma matrix
        :param x0: origem
        :param y0: origem
        :param w: largura de uma posição
        :param h: Altura de uma posição
        :param valor: matriz numpy 2d
        :return: sem retorno
        """
        px=0
        py=0
        for x in range(x0,x0+valor.shape[1]*w,w):
            for y in range(y0+valor.shape[0]*h,y0,-h):
                label=str(valor[py,px])
                len_label=len(label)
                self.ax1.text(x+w/2-0.9*len_label, y+h/2-1, label,fontsize=18,color='r')
                self.rect(x, y, w, h)
                py+=1
            py=0
            px+=1


    def my_grid(self,x0,y0,pasx,pasy,nline,ncol,valor):

        for x in range(x0,x0+ncol*pasx,pasx):
            for y in range(y0,y0+ nline*pasy, pasy):
                self.ax1.text(x + pasx / 2, y + pasy / 2, "$"+str(valor)+"$")
                self.rect(x, y, pasx, pasy)

    def line(self,x0,y0,x1,y1):
        self.ax1.plot([x0,x1],[y0,y1],color="b")
