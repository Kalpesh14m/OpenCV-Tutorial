import cv2
import numpy as np

img1 = cv2.imread('Images/3D-Matplotlib.png',cv2.IMREAD_COLOR)
img2 = cv2.imread('Images/mainsvmimage.png',cv2.IMREAD_COLOR)

# # Add Two Images
# add = img1 + img2
# cv2.imshow('add',add)

# # Add Two images using Add method
# add = cv2.add(img1, img2)
# cv2.imshow('add',add)

weighted = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
