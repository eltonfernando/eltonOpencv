import cv2
from .save_mp4 import Video
if __name__ =="__main__":
    "teste"
    cap=cv2.VideoCapture(0)

    vs=Video()
    while cap.isOpened():
        _,frame=cap.read()
        vs.write_frame(frame)
        cv2.imshow("janela",frame)
        cv2.
