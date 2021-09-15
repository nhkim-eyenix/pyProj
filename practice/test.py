import numpy as np
import cv2

image = cv2.imread("1.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("Leo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()