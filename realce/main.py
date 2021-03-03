import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
dados=np.array([1,2,2,3,4,5,5])
plt.title("Velocidade")
plt.ylabel("Tempo (s)")
plt.xlabel("Amostra")
#plt.hist(dados)
#plt.show()
clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(2,2))
img_bgr= cv2.imread("jetson.jpg")[600:-700, 950:-800]
img_hsv=cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
print(img_hsv.shape)
inicio=time.time()
hist=cv2.equalizeHist(img_hsv[:, :, 2])
stop=time.time()-inicio
print(stop)
inicio=time.time()

cl1 = clahe.apply(img_hsv[:, :, 2])
print(time.time()-inicio)
#plt.hist(img_hsv[:, :, 2].flatten(), color="b", bins=255,label="Original")
#plt.hist(cl1.flatten(),color="r",bins=255,label="Equalizada")
#plt.legend()
#plt.show()
x=[0.0054302215576171875,0.009469032287597656,0.013411760330200195]
y=["equalizeHist","clahe 10x10","clahe 8x8"]
plt.bar(y,x)
plt.show()
img_hsv[:, :, 2]=cl1
saidahsvcl1=cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
concat=cv2.hconcat((img_bgr,saidahsvcl1))
cv2.imwrite("equalizeHist.jpg",cv2.resize(concat,None,None,0.4,0.4))

cv2.imshow("janela", cv2.resize(img_bgr, None, None, 0.5, 0.5))

cv2.imshow("adap",cv2.resize(saidahsvcl1, None, None, 0.5, 0.5))
cv2.waitKey(0)

if __name__=="__main__":
    pass