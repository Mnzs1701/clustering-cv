import cv2
import numpy
x=cv2.imread("pikachu.png",1)
y=cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)

cv2.imshow("image",y)
blur = cv2.GaussianBlur(y,(11,11),0)
cv2.waitKey(0)
cv2.imshow("image",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()