

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('b.jpg',0)
img = cv.medianBlur(img,5)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
"""
img = cv2.VideoCapture('videoplayback.mp4')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval2, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('original',img)

cv2.imshow('threshold2', threshold2)
cv2.imshow('otsu', otsu





#ARKAPLAN SİLDİRME -----

cap = cv2.VideoCapture('videoplayback.mp4')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()
while (1):
    ret, img = cap.read()
    img = cv2.medianBlur(img, 5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(img)
    th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    #th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    #th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
               ]
    images = [img, th1]
    for i in range(2):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if cv2.waitKey(27) == ord('q'):
        break

cap.release()
"""



