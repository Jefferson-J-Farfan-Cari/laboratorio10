import cv2
import numpy as np

image = cv2.imread('dog.png')
kernel = np.ones((5, 5), np.uint8)

open = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.imshow('ORIGINAL', image)
cv2.imshow('OPEN', open)
cv2.waitKey()
cv2.destroyAllWindows()
