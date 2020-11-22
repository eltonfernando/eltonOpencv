from PyQt5.uic import loadUi
from PyQt5.QtWidgets import  QMainWindow,QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from process import Video

class Janela(QMainWindow):
    def __init__(self):
        super(Janela,self).__init__()
        loadUi("interface.ui", self)
        self.vs=Video()
        self.vs.change_pixmap.connect(self.frame_update)

    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        if not self.vs.isRunning():
            self.vs.stop=False
            self.vs.start()

    @pyqtSlot()
    def on_pushButton_stop_clicked(self):
        self.vs.stop=True

    @pyqtSlot(QImage)
    def frame_update(self,image):
        self.label_video.setPixmap(QPixmap.fromImage(image))

if __name__ == "__main__":
    import sys
    app=QApplication(sys.argv)
    my_janela=Janela()
    my_janela.show()
    app.exec_()


