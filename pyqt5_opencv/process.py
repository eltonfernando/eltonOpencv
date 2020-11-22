import cv2
from PyQt5.QtGui import QImage
from PyQt5.QtCore import pyqtSignal,QThread

class Video(QThread):

    change_pixmap = pyqtSignal(QImage)

    def __init__(self):
        super(Video, self).__init__()
        self.stop=False

    def run(self):
        cap=cv2.VideoCapture(0)
        while cap.isOpened():
            ret,frame=cap.read()
            if not ret:
                print("sem frame")
                cap.release()
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape

            convertToQtFormat = QImage(frame, w, h, ch*w, QImage.Format_RGB888)

            self.change_pixmap.emit(convertToQtFormat)
            if self.stop:
                cap.release()
                break

if __name__ == "__main__":
    cv=Video()
    cv.run()