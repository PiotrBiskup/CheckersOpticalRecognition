import cv2
import numpy as np

img = cv2.imread('zdj/7.jpg',0)

res = cv2.resize(img,None,fx=0.18, fy=0.18, interpolation = cv2.INTER_CUBIC)
res = cv2.medianBlur(res,5)
cimg = cv2.cvtColor(res,cv2.COLOR_GRAY2BGR)

#circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,100,param1=35,param2=15,minRadius=0,maxRadius=0) #20, 25
#circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,20,param1=35,param2=15,minRadius=20,maxRadius=25) #20, 25

circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,20,param1=35,param2=15,minRadius=20,maxRadius=25) #20, 25

circles = np.uint16(np.around(circles))

index = 1

for i in circles[0,:]:
    print(str(index) + ': ' + str(i))
    index += 1
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
