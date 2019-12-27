import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    ret, img = cap.read()
    cv2.imshow('deneme', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if cv2.waitKey(27) == ord('q'):
        break

cap.release()