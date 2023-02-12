"""
Autor: Elton fernandes dos Santos

ob = Video()
ob.write_frame(frame)
# novo video
ob.set_name_out("novo")
"""

from logging import getLogger
import cv2


class SaveVideo:
    def __init__(self, fps=30, out_name="saida") -> None:
        self.log = getLogger(__name__)
        self.fps = fps
        self.out_name = out_name
        self.ob_write = None
        self.fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    def split_video_rename(self, name_out: str) -> None:
        self.ob_write = None
        if not name_out.endswith(".mp4"):
            name_out += ".mp4"
        self.out_name = name_out

    def write_frame(self, frame) -> None:
        if self.ob_write is None:
            self.ob_write = cv2.VideoWriter(
                self.out_name,
                self.fourcc,
                self.fps,
                (frame.shape[1], frame.shape[0]),
                True,
            )
        else:
            self.ob_write.write(frame)

    def close(self) -> None:
        try:
            self.ob_write.release()
        except Exception as error:
            print(error)

    def __del__(self) -> None:
        self.close()


if __name__ == "__main__":
    "teste"
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("nao pode abrir camera")

    vs = SaveVideo()
    while cap.isOpened():
        flag, frame = cap.read()
        if not flag:
            break
        cv2.imshow("janela", frame)
        vs.write_frame(frame)
        if cv2.waitKey(1) == ord("q"):
            break
    vs.close()
