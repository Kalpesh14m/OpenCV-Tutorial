import numpy as np
import cv2

img = cv2.imread('Images/watch.png', cv2.IMREAD_COLOR)
img[55,55] = [255,0,0]

#ROI
# img[50:150, 50:150] = [255,0,0]

watch_face = img[80:150, 70:180]

# cv2.imshow('image', watch_face)

img[0:70, 0:110] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
