
import cv2
class MeidianFow():
    def __init__(self):
        self.tracker =None
    def start(self,frame, bbox):
        self.tracker = cv2.TrackerKCF_create()
        (x,y),(x2,y2)=bbox
        w=x2-x
        h=y2-y
        self.ok = self.tracker.init(frame,[x,y,w,h])

    def predict(self,frame):
        ok, new_bbox = self.tracker.update(frame)
        if ok:
            (x, y, w, h) = [int(v) for v in new_bbox]

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,0),2,1)
            print("box tracker",x,y,w,h)
            return [x,y,w,h]
        else:
            return None
