import cv2

imagen1 = cv2.imread('dog.png')
imagen2 = cv2.imread('dog_HSV.png')
concat_horizontal = cv2.hconcat([imagen1, imagen2])
cv2.imshow('Images together', concat_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
