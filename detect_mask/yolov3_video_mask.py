"""
autor: Elton Fernandes dos Santos
File: yolov3_video_mask.py
"""
import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)
writer = None
h, w = None, None

CLASSES = open('./data/classes.names').read().strip().split("\n")
weightsPath = './weights/mask_yolov3-tiny.weights'
configPath = './cfg/mask_yolov3-tiny.cfg'

net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

layers_names_all = net.getLayerNames()
layers_names_output = \
    [layers_names_all[i[0] - 1] for i in net.getUnconnectedOutLayers()]

probability_minimum = 0.4
threshold = 0.3
colours = np.array([[255,0,0],[0,0,255]])

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break
    if w is None or h is None:
        h, w = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)

    net.setInput(blob)

    start = time.time()
    output_blobs = net.forward(layers_names_output)
    end = time.time()
    bounding_boxes = []
    confidences = []
    class_numbers = []

    for result in output_blobs:
        print("up")
        print(result)
        for detected_objects in result:
            scores = detected_objects[5:]
            #print(scores)

            class_current = np.argmax(scores)
            confidence_current = scores[class_current]

            if confidence_current > probability_minimum:
                box_current = detected_objects[0:4] * np.array([w, h, w, h])
                x_center, y_center, box_width, box_height = box_current
                print(box_width)
                x_min = int(x_center - (box_width / 2))
                y_min = int(y_center - (box_height / 2))

                bounding_boxes.append([x_min, y_min,
                                       int(box_width), int(box_height)])
                confidences.append(float(confidence_current))
                class_numbers.append(class_current)

    results = cv2.dnn.NMSBoxes(bounding_boxes, confidences,
                               probability_minimum, threshold)

    if len(results) > 0:
        for i in results.flatten():
            x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
            box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]

            colour_box_current = colours[class_numbers[i]].tolist()

            cv2.rectangle(frame, (x_min, y_min),
                          (x_min + box_width+10, y_min + box_height+10),
                          colour_box_current, 2)

            text_box_current = '{}: {:.4f}'.format(CLASSES[int(class_numbers[i])],
                                                   confidences[i])

            cv2.putText(frame, text_box_current+" FPS "+str(round(1/(end-start))), (x_min, y_min-2),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, colour_box_current, 2)

    cv2.imshow("frame",frame)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

    if writer is None:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter('saida.mp4', fourcc, 30,
                                 (frame.shape[1], frame.shape[0]), True)

    writer.write(frame)

cap.release()
writer.release()

