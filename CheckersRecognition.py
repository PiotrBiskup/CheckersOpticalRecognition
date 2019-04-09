import cv2
import numpy as np


def check_vertex_list(vertex_list):
    if vertex_list[0][0] <= vertex_list[1][0] and vertex_list[2][0] >= vertex_list[3][0]:
        return vertex_list

    elif vertex_list[0][0] >= vertex_list[1][0] and vertex_list[2][0] <= vertex_list[3][0]:
        vertex_list[0][0], vertex_list[1][0] = vertex_list[1][0], vertex_list[0][0]
        vertex_list[2][0], vertex_list[3][0] = vertex_list[3][0], vertex_list[2][0]
        return vertex_list

    elif vertex_list[0][0] <= vertex_list[1][0] and vertex_list[2][0] <= vertex_list[3][0]:
        vertex_list[2][0], vertex_list[3][0] = vertex_list[3][0], vertex_list[2][0]
        return vertex_list

    elif vertex_list[0][0] >= vertex_list[1][0] and vertex_list[2][0] >= vertex_list[3][0]:
        vertex_list[0][0], vertex_list[1][0] = vertex_list[1][0], vertex_list[0][0]
        return vertex_list


def increase_board_area(list):
    list[0][0] -= 10
    list[0][1] -= 10
    list[1][0] += 10
    list[1][1] -= 10
    list[2][0] += 10
    list[2][1] += 10
    list[3][0] -= 10
    list[3][1] += 10

    return list


#testowanie dla roznych kolorow prostokatow
# lower_red = np.array([0, 100, 100])
# upper_red = np.array([10, 255, 255])
#
# lower_yellow = np.array([20, 100, 100])
# upper_yellow = np.array([30, 255, 255])


lower_blue = np.array([100, 70, 70])  # 100,50,50
upper_blue = np.array([130, 255, 255])

#wczytanie zdjecia
img = cv2.imread('zdj/b4.jpeg')

#zmniejszenie obrazu
res = cv2.resize(img, None, fx=0.18, fy=0.18, interpolation=cv2.INTER_CUBIC)

cv2.imshow('obrazek', res)
cv2.waitKey(0)

#zamiana na HSV
hsv = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)

#stworzenie obrazu binarnego z pikseli z podanego zakresu
mask = cv2.inRange(hsv, lower_blue, upper_blue)

#usuniecie zle wykrytych pojdynczych pikseli
kernel = np.ones((6, 6), np.uint8)
erosion = cv2.erode(mask, kernel, iterations=1)
dilation = cv2.dilate(erosion, kernel, iterations=1)

#znalezienie konturow
image, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#rysowanie konturow
img2 = cv2.drawContours(image, contours, -1, (128, 255, 187), 3)

#wyliczenie srodkow masy prostokatow
list_of_points = []

for i in contours:
    cnt = i
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    img2 = cv2.line(img2, (cx, cy), (cx, cy), (128, 255, 187), 5)
    list_of_points.append([cx, cy])


list_of_points.reverse()
print('1. ' + str(list_of_points))
checked_list_of_points = check_vertex_list(list_of_points)
print('2. ' + str(checked_list_of_points))
increased_list_of_points = increase_board_area(checked_list_of_points)


pts1 = np.float32([increased_list_of_points[0], increased_list_of_points[1], increased_list_of_points[2],
                   increased_list_of_points[3]])

pts2 = np.float32([[0, 0], [600, 0], [600, 600], [0, 600]])

#stworzenie macierzy tranformacji perspektywicznej
M = cv2.getPerspectiveTransform(pts1, pts2)

#transformacja perspektywiczna
dst = cv2.warpPerspective(res, M, (600, 600))

cv2.imshow("obrazek", dst)
cv2.waitKey()
cv2.destroyAllWindows()





#img = cv2.imread('zdj/7.jpg',0)
#
# res = cv2.resize(img,None,fx=0.18, fy=0.18, interpolation = cv2.INTER_CUBIC)
# res = cv2.medianBlur(res,5)
# cimg = cv2.cvtColor(res,cv2.COLOR_GRAY2BGR)
#
# #circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,100,param1=35,param2=15,minRadius=0,maxRadius=0) #20, 25
# #circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,20,param1=35,param2=15,minRadius=20,maxRadius=25) #20, 25
#
# circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,20,param1=35,param2=15,minRadius=20,maxRadius=25) #20, 25
#
# circles = np.uint16(np.around(circles))
#
# index = 1
#
# for i in circles[0,:]:
#     print(str(index) + ': ' + str(i))
#     index += 1
#     # draw the outer circle
#     cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#     # draw the center of the circle
#     cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
#
# cv2.imshow('detected circles',cimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()