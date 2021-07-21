"""
Autor: Elton fernandes dos Santos

ob = Video()
ob.write_frame(frame)
# novo video
ob.set_name_out("novo")
"""
import cv2


class Video:

    def __init__(self, format="mp4", fps=30, out_name="saida"):
        self.format = format
        self.fps = fps
        self.out_name = out_name
        self.fourcc = None
        self.ob_write = None
        self.set_fourcc()

    def set_name_out(self, name_out):
        self.ob_write = None
        self.out_name = name_out
        self.set_fourcc()

    def set_fourcc(self):
        self.out_name += "." + self.format
        if self.format == 'mp4':
            self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    def write_frame(self,frame):
        if self.ob_write is None:
            self.ob_write = cv2.VideoWriter(self.out_name, self.fourcc, self.fps, (frame.shape[1], frame.shape[0]), True)
        else:
            self.ob_write.write(frame)
    def close(self):
        self.ob_write.release()
if __name__ =="__main__":
    "teste"
    cap=cv2.VideoCapture(0)

    vs=Video()
    while cap.isOpened():

        _,frame=cap.read()
        vs.write_frame(frame)
