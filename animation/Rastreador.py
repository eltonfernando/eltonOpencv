
import cv2
class MeidianFow():
    def __init__(self):
        self.tracker =None
    def start(self,frame, bbox):
        self.ok = self.tracker.init(frame, tuple(bbox))
        self.tracker=cv2.TrackerMedianFlow_create()
    def predict(self,frame,bbox):
        ok, new_bbox = self.tracker.update(frame)
        if ok:
            (x, y, w, h) = [int(v) for v in new_bbox]

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,0),10,1)
            print("tran",x,y,w,h)
            return [x,y,w,h]
        else:
            print("falhar ao rastrear",bbox)
            return bbox