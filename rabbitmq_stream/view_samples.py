import cv2
import numpy as np
from core import Consumer


class VideoView():
    def __init__(self):
        self.consumer = Consumer("frame")
        self.consumer.start(on_message=self.on_message)

    @staticmethod
    def on_message(chan, method_frame, header_frame, body, userdata=None):
        """Called when a message is received. Log message and ack it."""
       # print(chan)
       # print(method_frame)

        body = np.frombuffer(body, np.uint8)
        img = cv2.imdecode(body,cv2.IMREAD_COLOR)
        cv2.imshow(method_frame.routing_key,img)
        cv2.waitKey(1)

        chan.basic_ack(delivery_tag=method_frame.delivery_tag)

if __name__ == "__main__":
    view = VideoView()