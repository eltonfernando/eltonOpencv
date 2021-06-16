"""
para cadastrar uma nova face na base seja o arquivo data_face.py
"""
import cv2
from process import CriaFaceRecongnition

cap = cv2.VideoCapture(0)

process_this_frame = True # pula um frame

face=CriaFaceRecongnition()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        raise NameError("frame invalido")

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame =cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)
    if process_this_frame:
        face.detection(rgb_small_frame)
        face.compare()
    print(face.face_names)

    face.draw(frame,resized=0.25)

    process_this_frame = not process_this_frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
