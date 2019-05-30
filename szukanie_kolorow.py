import numpy as np
import cv2

green = np.uint8([[[233, 249, 255]]])
hsvGreen = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsvGreen)
lowerLimit = (hsvGreen[0][0][0]-10,100,100)
upperLimit = (hsvGreen[0][0][0]+10,255,255)
print(upperLimit)
print(lowerLimit)

# t1 = cv2.imread('zdj/t1.jpg')
# t2 = cv2.imread('zdj/t2.jpg')
# t3 = cv2.imread('zdj/t3.jpg')
# t4 = cv2.imread('zdj/kolor.png')
#
# res1 = cv2.resize(t1, None, fx=0.18, fy=0.18, interpolation=cv2.INTER_CUBIC)
# res2 = cv2.resize(t2, None, fx=0.18, fy=0.18, interpolation=cv2.INTER_CUBIC)
# res3 = cv2.resize(t3, None, fx=0.18, fy=0.18, interpolation=cv2.INTER_CUBIC)
#
#
# hsv1 = cv2.cvtColor(res1, cv2.COLOR_BGR2HSV)
# hsv2 = cv2.cvtColor(res2, cv2.COLOR_BGR2HSV)
# hsv3 = cv2.cvtColor(res3, cv2.COLOR_BGR2HSV)
# hsv4 = cv2.cvtColor(t4, cv2.COLOR_BGR2HSV)

# cv2.imshow('t1', hsv1)
# cv2.imshow('t2', hsv2)
# cv2.imshow('t3', hsv3)
# cv2.imshow('t4', hsv4)
#
# cv2.waitKey()
# cv2.destroyAllWindows()
