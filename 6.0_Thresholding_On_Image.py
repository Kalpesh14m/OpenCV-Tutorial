import cv2
import numpy as np

img = cv2.imread('Images/bookpage.jpg', cv2.IMREAD_COLOR)

#Convert Imgae into threshold image increase brightness
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

#Convert Imgae into grayscale
grayscale = cv2.cvtColor(threshold, cv2.COLOR_RGB2GRAY)

#Threshold on Grayscale Imgae to increase more brightness
retval2, threshold2 = cv2.threshold(grayscale, 12, 255, cv2.THRESH_BINARY)

#AdaptiveThreshold on Grayscale Imgae to increase more brightness and make SHARP
gaus = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#Threshold on Grayscale Imgae to increase more brightness
retval2, otsu = cv2.threshold(grayscale, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('Orignal', img)
cv2.imshow('Threshold1', threshold)
cv2.imshow('grayscale', grayscale)
cv2.imshow('Threshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
