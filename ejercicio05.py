import cv2
import numpy as np

image = cv2.imread('dog.png')
kernel = np.ones((5, 5), np.uint8)

close = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imshow('ORIGINAL', image)
cv2.imshow('CLOSE', close)
cv2.waitKey()
cv2.destroyAllWindows()
