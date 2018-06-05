import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('Images/Demo_15_Record_People_Walk.mp4')

cap.set(3,100)
cap.set(4,500)

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('Orignal',frame)
    cv2.imshow('FG Converted', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
