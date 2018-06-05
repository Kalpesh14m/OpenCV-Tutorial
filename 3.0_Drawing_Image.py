import cv2
import numpy as np

img = cv2.imread('Images/watch.png',cv2.IMREAD_COLOR)

#draw Line
cv2.line(img, (10,10), (150,150), (255, 0, 0), 15)
#draw Rectangle
cv2.rectangle(img, (10,10), (150,150), (0, 255, 0), 15)
#draw Circle
cv2.circle(img, (50,50), 50, (0, 0, 255), -1)
#draw Polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 0, 0), 5)
#Font
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, 'Kalpesh Demo!!', (0, 130), font, 1, (0,255,255), 3, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
