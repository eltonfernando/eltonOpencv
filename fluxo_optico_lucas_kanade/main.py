import numpy as np
import cv2
#from save_mp4 import Video
cap=cv2.VideoCapture("0")
prev_gray = None
#save=Video()

def mause_point(event, x, y, flags, params):
  global point, point_selected, old_points
  if event == cv2.EVENT_LBUTTONDOWN:
    point = (x, y)
    point_selected = True
    old_points = np.array([[x, y]], dtype=np.float32)

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mause_point)

point_selected = False
point = ()
old_points = np.array([[]])
lk_params = dict(winSize=(21, 21),
                 maxLevel=5,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 3, 0.01))
while cap.isOpened():
  _, frame = cap.read()

  curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  if prev_gray is None:
    prev_gray=curr_frame.copy()
  if point_selected is True:
    new_points, status, error = cv2.calcOpticalFlowPyrLK(prev_gray, curr_frame, old_points, None, **lk_params)
    print(new_points,old_points)
    prev_gray = curr_frame.copy()
    old_points = new_points
    px,py=int(new_points[0][0]),int(new_points[0][1])
    cv2.circle(frame, (px,py), 2, (0, 255, 255),cv2.FILLED)
    cv2.rectangle(frame,(px-10,py-10),(px+10,py+10),(0,0,255),2)

    #save.write_frame(frame)
    #print(frame.shape)

  cv2.imshow("Frame",frame)
  k = cv2.waitKey(230)
  if k==ord("q"):
    #save.close()
    break
