import cv2
import numpy as np
import matplotlib.pyplot as plot

img = cv2.imread('Images/watch.png',cv2.WINDOW_NORMAL)

#Show Image using cv3 library
cv2.imshow('image',img)
#Close window when press any key
cv2.waitKey(0)
#Destroy CV2 object
cv2.destroyAllWindows()

#Open image using matplotlib library
# plot.imshow(img, cmap='gray', interpolation='bicubic')
#Edit on Image
# plot.plot([50,100], [80,100], 'c', linewidth=5)
#Show image
# plot.show()

#Save Image
cv2.imwrite('Generated_Image/New_Img.png',img)
