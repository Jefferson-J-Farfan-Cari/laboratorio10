import cv2

img1 = cv2.imread('dog.png')
value = 20

hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

lim = 255 - value
v[v > lim] = 255
v[v <= lim] += value

final_hsv = cv2.merge((h, s, v))
img2 = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

concat_horizontal = cv2.hconcat([img1, img2])

cv2.imshow('Brightness', concat_horizontal)
cv2.waitKey()
cv2.destroyAllWindows()
