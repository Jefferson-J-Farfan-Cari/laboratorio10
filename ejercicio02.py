import cv2

image = cv2.imread('dog.png')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imwrite('dog_HSV.png', hsv)

cv2.imshow('HSV', hsv)
cv2.waitKey()
cv2.destroyAllWindows()
