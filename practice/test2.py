import cv2
import numpy as np

img = np.full((450, 450, 3), 255, dtype = np.uint8) #350x350 size, white background

cv2.line(img, (50, 50), (100, 50), (0, 0, 255))     # Red
cv2.line(img, (150, 50), (200, 50), (0, 255, 0))    # Green
cv2.line(img, (250, 50), (300, 50), (255, 0, 0))    # Blue

cv2.rectangle(img, (200, 200), (400, 400), (255, 0, 0), -1) #fill with blue
cv2.ellipse(img, (350, 300), (50, 50), 0, 0, 180, (0, 255, 0))

cv2.imshow('Line', img)
cv2.waitKey()
cv2.destroyAllWindows()
