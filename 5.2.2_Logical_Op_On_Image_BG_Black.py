import cv2
import numpy as np

img1 = cv2.imread('Images/FGImg.png',cv2.IMREAD_COLOR)
# cv2.imshow("img1",img1)
logo = cv2.imread('Images/imLogo.png',cv2.IMREAD_COLOR)
# cv2.imshow('img2',logo)

rows, cols, channel = logo.shape
roi = img1[0:rows, 0:cols]
# cv2.imshow('roi',roi)

img2gray = cv2.cvtColor(logo, cv2.COLOR_RGB2GRAY)
# cv2.imshow('img2gray', img2gray)

ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
# cv2.imshow('mask_inv', mask_inv)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('img1_bg', img1_bg)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(logo,logo,mask = mask)
cv2.imshow('img2_fg', img2_fg)

dst = cv2.add(img1_bg,img2_fg)
cv2.imshow('dst', dst)

img1[0:rows, 0:cols] = dst

cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
