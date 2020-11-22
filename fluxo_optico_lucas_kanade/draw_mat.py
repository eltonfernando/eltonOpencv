import cv2
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib
import draw

#from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)
# #params = {'backend': 'ps',
#       'axes.labelsize': 16,
#       'axes.titlesize':20,
#       #'text.fontsize': 10,
#       'legend.fontsize': 16,
#       'xtick.labelsize': 16,
#       'ytick.labelsize': 16,
#      # 'text.usetex': True,
#       #'text.latex.unicode': True,
#       'figure.figsize': [10,10]}
#matplotlib.rcParams.update(params)

fig =plt.figure(figsize=(14,14))
ax1 = fig.add_subplot(1,1,1)
plt.grid(False)
plt.style.use("grayscale")
mat_valor=cv2.imread("roi.png")


#plt.show()
print("aqui")
ax1.clear()
pen=draw.Draw(ax1)
pen.mat_grid(2,2,10,10,mat_valor[:,:0])
print(mat_valor)
#plt.imshow(mat_valor)
plt.savefig("mat.png",dpi=90)
plt.show()


# kernel=np.ones((3,3))/9
# ft=cv2.filter2D(mat_valor,-1,kernel)
# plt.imshow(ft)
# plt.show()

#ax1.clear()
#pen=draw.Draw(ax1)
#pen.mat_grid(2,2,3,3,mat_valor)
#plt.show()