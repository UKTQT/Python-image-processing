import numpy as np
import cv2
cap = cv2.VideoCapture('iha.mp4')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('GORUNTU',fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if cv2.waitKey(27) == ord('q'):
        break

cv2.imwrite('frame.png',fgbg)
cap.release()
cv2.destroyAllWindows()