import cv2
import numpy as np


def check_vertex_list(vertex_list):
    if vertex_list[0][0] <= vertex_list[1][0] and vertex_list[2][0] >= vertex_list[3][0]:
        return vertex_list

    elif vertex_list[0][0] >= vertex_list[1][0] and vertex_list[2][0] <= vertex_list[3][0]:
        vertex_list[0], vertex_list[1] = vertex_list[1], vertex_list[0]
        vertex_list[2], vertex_list[3] = vertex_list[3], vertex_list[2]
        return vertex_list

    elif vertex_list[0][0] <= vertex_list[1][0] and vertex_list[2][0] <= vertex_list[3][0]:
        vertex_list[2], vertex_list[3] = vertex_list[3], vertex_list[2]
        return vertex_list

    elif vertex_list[0][0] >= vertex_list[1][0] and vertex_list[2][0] >= vertex_list[3][0]:
        vertex_list[0], vertex_list[1] = vertex_list[1], vertex_list[0]
        return vertex_list


def increase_board_area(vertex_list):
    vertex_list[0][0] -= 10
    vertex_list[0][1] -= 10
    vertex_list[1][0] += 10
    vertex_list[1][1] -= 10
    vertex_list[2][0] += 10
    vertex_list[2][1] += 10
    vertex_list[3][0] -= 10
    vertex_list[3][1] += 10

    return vertex_list


def board_perspective_transform(image):
    # testowanie dla roznych kolorow prostokatow
    # lower_red = np.array([0, 100, 100])
    # upper_red = np.array([10, 255, 255])
    #
    # lower_yellow = np.array([20, 100, 100])
    # upper_yellow = np.array([30, 255, 255])

    lower_blue = np.array([100, 70, 70])  # 100,50,50
    upper_blue = np.array([130, 255, 255])

    # zmniejszenie obrazu
    res = cv2.resize(image, None, fx=0.18, fy=0.18, interpolation=cv2.INTER_CUBIC)

    # cv2.imshow('obrazek', res)
    # cv2.waitKey(0)

    # zamiana na HSV
    hsv = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)

    # cv2.imshow('obrazek', hsv)
    # cv2.waitKey(0)

    # stworzenie obrazu binarnego z pikseli z podanego zakresu
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # cv2.imshow('obrazek', mask)
    # cv2.waitKey(0)

    # usuniecie zle wykrytych pojdynczych pikseli
    kernel = np.ones((6, 6), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=1)

    # znalezienie konturow
    image, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # rysowanie konturow
    img2 = cv2.drawContours(image, contours, -1, (128, 255, 187), 3)

    # wyliczenie srodkow masy prostokatow
    list_of_points = []

    for i in contours:
        cnt = i
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        img2 = cv2.line(img2, (cx, cy), (cx, cy), (128, 255, 187), 5)
        list_of_points.append([cx, cy])

    # cv2.imshow('obrazek', img2)
    # cv2.waitKey(0)

    list_of_points.reverse()
    # print('1. ' + str(list_of_points))
    checked_list_of_points = check_vertex_list(list_of_points)
    # print('2. ' + str(checked_list_of_points))
    increased_list_of_points = increase_board_area(checked_list_of_points)

    pts1 = np.float32([increased_list_of_points[0], increased_list_of_points[1], increased_list_of_points[2],
                       increased_list_of_points[3]])

    pts2 = np.float32([[0, 0], [600, 0], [600, 600], [0, 600]])

    # stworzenie macierzy tranformacji perspektywicznej
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # transformacja perspektywiczna
    dst = cv2.warpPerspective(res, M, (600, 600))

    # cv2.imshow("obrazek", dst)
    # cv2.waitKey()

    return dst


def find_checkers(image):

    # dodanie rozmycia zeby lepiej wykrywac kola
    blurred_img = cv2.medianBlur(image, 7)
    gray_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1, 30, param1=35, param2=22, minRadius=25,
                               maxRadius=35)  # 20, 25

    if circles is not None:
        circles = np.uint16(np.around(circles))
        # index = 1
        # for i in circles[0, :]:
        #     # print(str(index) + ': ' + str(i))
        #     index += 1
        #     # draw the outer circle
        #     cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        #     # draw the center of the circle
        #     cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

    # cv2.imshow('obrazek', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return circles


def find_board_squares():
    x = 24
    y = 24
    inc = 69
    squares_coord = []

    for j in range(0, 8):
        for i in range(0, 8):
            squares_coord.append([[x, y], [x + inc, y + inc]])
            x += inc
        x = 24
        y += inc

    # print(squares_cordinates)
    # for i in squares_cordinates:
    #     cv2.rectangle(img, (i[0][0], i[0][1]), (i[1][0], i[1][1]), (122, 122, 122), 4)
    #
    # cv2.imshow('image', img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    return squares_coord

def find_colored_checkers(image, checkers, squares):
    cv2.imshow('obrazek', image)
    cv2.waitKey(0)
    # lower_black = np.array([0, 0, 0])
    # upper_black = np.array([180, 200, 30])
    #
    # cv2.imshow('obrazek', image)
    # cv2.waitKey(0)
    #
    # # zamiana na HSV
    # hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #
    #
    # # stworzenie obrazu binarnego z pikseli z podanego zakresu
    # mask = cv2.inRange(hsv, lower_black, upper_black)
    #
    # cv2.imshow('obrazek', mask)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('obrazek', gray_scale)
    cv2.waitKey(0)

    ret, th = cv2.threshold(gray_scale, 180, 255, cv2.THRESH_BINARY)
    cv2.imshow('obrazek', th)
    cv2.waitKey(0)

    # usuniecie zle wykrytych pojdynczych pikseli
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(th, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=1)

    cv2.imshow('obrazek', dilation)
    cv2.waitKey(0)


    cv2.destroyAllWindows()


    return [], []


img = cv2.imread('zdj/b8.jpeg')
img_transformed = board_perspective_transform(img)
checkers_list = find_checkers(img_transformed)
squares_coordinates = find_board_squares()
find_colored_checkers(img_transformed, checkers_list, squares_coordinates)




