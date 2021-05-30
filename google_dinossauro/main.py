#https://github.com/google/mediapipe/blob/master/docs/solutions/hands.md
import numpy as np
import cv2
import pyautogui
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
PRESSED_SPACE=False
PRESSED_DOWN=False

pyautogui.press("space")
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=1,
    static_image_mode=False) as hands:
  while cap.isOpened():
    success, image = cap.read()

    if not success:
      continue
    image=cv2.flip(image, 1)
    image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image.flags.writeable = False

    results = hands.process(image_RGB)

    if results.multi_hand_landmarks:
        image_height, image_width, _ = image.shape
        annotated_image = image.copy()
        for hand_landmarks in results.multi_hand_landmarks:

            dedao_x=hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width
            dedao_y=hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height
            dedao=(int(dedao_x),int(dedao_y))
            indicador_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width
            indicador_y=hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height
            indicador=(int(indicador_x),int(indicador_y))

            distancia=int(np.sqrt((indicador_x-dedao_x)**2+(indicador_y-dedao_y)**2))

            COLOR=(0,255,0)
            if distancia>80:
                COLOR=(255,0,0)
                if not PRESSED_SPACE:
                    print("tecla")
                    pyautogui.press("space")
                    PRESSED_SPACE=True
            else:
                PRESSED_SPACE=False
                if distancia<20:
                    if not PRESSED_DOWN:
                        print("tecla")
                        pyautogui.keyDown('Down')
                        PRESSED_DOWN=True
                    COLOR=(0,0,255)
                else:
                    if PRESSED_DOWN:
                        print("tecla")
                        pyautogui.keyUp('Down')
                        PRESSED_DOWN=False

            cv2.line(image, (dedao), (indicador), COLOR, 2, cv2.LINE_AA)
            cv2.circle(image,indicador,4,(255,0,255),2,cv2.LINE_AA)
            cv2.circle(image,dedao, 4, (255, 0, 0), 2, cv2.LINE_AA)

            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('visioncompy', image)
    if cv2.waitKey(30) & 0xFF == 27:
      break
cap.release()
