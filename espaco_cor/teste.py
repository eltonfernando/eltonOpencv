from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
cap=cv2.VideoCapture("/home/elton/Videos/ticonsulte_processo/video_shoping/vlc-record-2020-07-22-11h03m24s-rtsp___177.21.30.184_5542_ch1_sub_av_stream-___.mp4")
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# loop over the image paths
while(cap.isOpened()):
    _,image=cap.read()
    image=image[4:220,194:490]
    #image=cv2.resize(image,None,None,0.5,0.5)
    #image = imutils.resize(image, width=min(400, image.shape[1]))
    orig = image.copy()
    # detect people in the image
    (rects, weights) = hog.detectMultiScale(image, winStride=(6, 6),padding=(8, 8), scale=1.05)
    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.circle(orig,(int(x+w/2),int(y+h/2)),3,(255,0,0),cv2.FILLED)
        cv2.rectangle(orig, (x+8, y+8), (x + w-8, y + h-8), (0, 0, 255), 2)
   # rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    #pick = non_max_suppression(rects, probs=None, overlapThresh=0.45)
    # draw the final bounding boxes
   # for (xA, yA, xB, yB) in pick:
   #     cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
    cv2.imshow("Before NMS", orig)
    #cv2.imshow("After NMS", image)
    cv2.waitKey(30)