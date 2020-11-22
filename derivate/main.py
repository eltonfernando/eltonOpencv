import cv2
import os
scale = 1
delta = 0
ddepth = cv2.CV_16S
local="./img/"
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('out.mp4', fourcc, 30, (1080,1080))

for frame in sorted(os.listdir(local)):
    frame = cv2.imread(local+frame)#[:,:520]
    # calcula derivada parcial em x
    grad_x = cv2.Sobel(frame, ddepth, 1, 0,ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_ISOLATED)
    # calcula derivada parcial em x
    grad_y = cv2.Sobel(frame, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_ISOLATED)

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    saida=cv2.vconcat((frame,grad))

    saida=cv2.resize(saida,(1080,1080))
    out.write(saida)
    cv2.imshow("janela", saida)
    #cv2.imwrite("out.jpg", saida)
    cv2.waitKey(10)