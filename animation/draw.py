import numpy as np
import cv2
class Rosto():
    def __init__(self,width,height):
        self.WIDTH=width
        self.HEIGHT =height
        self.LEN_RAIO_OLHO=40
        self.rosto=np.zeros((self.HEIGHT,self.WIDTH,3),dtype=np.uint8)

    def start(self):
        self.center_olho_direito = self._rescale_percente(75, 40)
        self.center_olho_esquedo = self._rescale_percente(25, 40)
        self._draw_olho()
        self._draw_boca()

    def update(self,x,y):
        self._draw_olho()
        self._draw_conea(x,y)

    def get_rosto(self):
        return self.rosto

    def _draw_boca(self):
        center = self._rescale_percente(50, 75)
        cv2.ellipse(self.rosto,
                    center=center,
                    axes=(120, 50),
                    angle=0,
                    startAngle=0,
                    endAngle=180,
                    color=(255, 255, 255),
                    thickness=cv2.FILLED)

    def _draw_olho(self):
        cv2.circle(self.rosto, self.center_olho_direito, self.LEN_RAIO_OLHO, (255, 255, 255), cv2.FILLED)
        cv2.circle(self.rosto, self.center_olho_esquedo, self.LEN_RAIO_OLHO, (255, 255, 255), cv2.FILLED)

    def _rescale_percente(self,x, y):
        return (int(x / 100 * self.WIDTH), int(y / 100 * self.HEIGHT))
    @staticmethod
    def _norma_vetor(vetor:tuple):
        return np.linalg.norm(vetor)

    def _draw_conea(self,x:int,y:int):
        cv2.circle(self.rosto, self.get_center_cornea_esquerda(x, y), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(self.rosto, self.get_center_cornea_direita(x, y), 10, (255, 0, 0), cv2.FILLED)

    def get_center_cornea_esquerda(self,x,y)->tuple:
        vetor_olho_esquerdo =x-self.center_olho_esquedo[0],y-self.center_olho_esquedo[1]
        profundidade = self.LEN_RAIO_OLHO * .7
        CX_OLHO_ESQUERDO,CY_OLHO_ESQUERDO=self.center_olho_esquedo
        cx = profundidade* (x - CX_OLHO_ESQUERDO) / self._norma_vetor(vetor_olho_esquerdo) + CX_OLHO_ESQUERDO
        cy = profundidade* (y - CY_OLHO_ESQUERDO) / self._norma_vetor(vetor_olho_esquerdo) + CY_OLHO_ESQUERDO
        return (int(cx),int(cy))

    def get_center_cornea_direita(self,x:int,y:int)->tuple:
        vetor_olho_direito = x - self.center_olho_direito[0], y - self.center_olho_direito[1]
        profundidade=self.LEN_RAIO_OLHO * .7
        cx = profundidade* (x - self.center_olho_direito[0]) / self._norma_vetor(vetor_olho_direito) + self.center_olho_direito[0]
        cy = profundidade* (y - self.center_olho_direito[1]) /self._norma_vetor(vetor_olho_direito) + self.center_olho_direito[1]
        return (int(cx),int(cy))
if __name__=="__main__":
    rosto=Rosto(400,400)
    rosto.start()
    rosto.update(20,20)
    cv2.imshow("Rosto",rosto.get_rosto())
    cv2.waitKey(0)
