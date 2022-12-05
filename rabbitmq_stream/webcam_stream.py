import cv2
from time import sleep
from core import Producer


class VideoCap():
    def __init__(self):
        self.queue = Producer(exchange="capiture",queue="frame")

    def start(self,id_video):
        self.queue.start()
        cap = cv2.VideoCapture(id_video)
        while cap.isOpened():
            ret, frame = cap.read()
            flag, bytes = cv2.imencode(".jpg",frame)
            if flag:
                self.queue.append_byte(bytes.tobytes())
            sleep(1/25)




if __name__ == "__main__":

    vs = VideoCap()
    vs.queue.set_routing_key("wbecam")
    vs.start(0)




