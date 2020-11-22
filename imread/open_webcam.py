import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    flag, frame = cap.read()
    cv2.imshow("janela", frame)
    cv2.waitKey(1)
