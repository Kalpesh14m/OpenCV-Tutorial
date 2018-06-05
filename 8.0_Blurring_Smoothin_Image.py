import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,100)
cap.set(4,300)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ## HSV Hue Sat Value
    ## RED
    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    res_red = cv2.bitwise_and(frame, frame, mask = mask_red)

    #Smooth Image
    kernal = np.ones((15, 15), np.float32)/ 225
    smoothed = cv2.filter2D(res_red, -1, kernal)

    #
    blur = cv2.GaussianBlur(res_red, (15, 15), 0)
    median = cv2.medianBlur(res_red, 15)
    bilateral = cv2.bilateralFilter(res_red, 15, 75, 75)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask_RED', mask_red)
    cv2.imshow('res_RED', res_red)
    # cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
