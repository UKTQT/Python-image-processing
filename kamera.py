import cv2
import numpy as np

cap = cv2.VideoCapture('iha.mp4')

while (1):
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    processedimg = np.where(img)
    processedimg = cv2.convertScaleAbs(img)
    ret1, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(gray, 0, 255, (cv2.THRESH_BINARY + cv2.THRESH_OTSU))
    #blur = cv2.GaussianBlur(processedimg, (5, 5), 0)
    ret3, th3 = cv2.threshold(gray, 0, 255, (cv2.THRESH_BINARY + cv2.THRESH_OTSU))

    cv2.imshow('deneHme',th1)
    cv2.imshow('deneKme', th2)
    cv2.imshow('deneme', th3)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if cv2.waitKey(27) == ord('q'):
        break

cap.release()