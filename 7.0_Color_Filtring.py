import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,100)
cap.set(4,500)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ## HSV Hue Sat Value
    ## RED
    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    res_red = cv2.bitwise_and(frame, frame, mask = mask_red)

    cv2.imshow('mask_RED', mask_red)
    cv2.imshow('res_RED', res_red)

    ##BLUE
    # lower_blue = np.array([50,50,150])
    # upper_blue = np.array([150,250,180])
    #
    # mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    # res_blue = cv2.bitwise_and(frame, frame, mask = mask_blue)
    #
    # cv2.imshow('mask_BLUE', mask_blue)
    # cv2.imshow('res_BLUE', res_blue)

    ##GREEN
    # lower_green = np.array([50,150,50])
    # upper_green = np.array([150,250,150])
    #
    # mask_green = cv2.inRange(hsv, lower_green, upper_green)
    # res_green = cv2.bitwise_and(frame, frame, mask = mask_green)
    #
    # cv2.imshow('mask_GREEN', mask_green)
    # cv2.imshow('res_GREEN', res_green)

    cv2.imshow('frame', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
