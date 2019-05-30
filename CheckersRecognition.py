import cv2
import numpy as np


def find_corners(vertex_list):

    xmin = vertex_list[0][0]
    xmax = vertex_list[0][0]
    ymin = vertex_list[0][1]
    ymax = vertex_list[0][1]

    for x in vertex_list:

        if x[0] < xmin:
            xmin = x[0]

        if x[0] > xmax:
            xmax = x[0]

        if x[1] < ymin:
            ymin = x[1]

        if x[1] > ymax:
            ymax = x[1]

    corners_list = []

    for x in vertex_list:

        if x[0] == xmin or x[0] == xmax or x[1] == ymin or x[1] == ymax:
            corners_list.append(x)

    return corners_list


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


def board_perspective_transform(source_image):
    # testowanie dla roznych kolorow prostokatow
    # lower_red = np.array([0, 100, 100])
    # upper_red = np.array([10, 255, 255])
    #
    # lower_yellow = np.array([20, 100, 100])
    # upper_yellow = np.array([30, 255, 255])

    lower_blue = np.array([84, 100, 100])  # 100,50,50  100, 70, 70     84,100,100
    upper_blue = np.array([104, 255, 255]) #130,255,255      104,255,255

    # zmniejszenie obrazu
    # res = cv2.resize(image, None, fx=0.18, fy=0.18, interpolation=cv2.INTER_CUBIC)

    # cv2.imshow('obrazek', source_image)
    # cv2.waitKey(0)

    # zamiana na HSV
    hsv = cv2.cvtColor(source_image, cv2.COLOR_BGR2HSV)

    # cv2.imshow('obrazek', hsv)
    # cv2.waitKey(0)

    # stworzenie obrazu binarnego z pikseli z podanego zakresu
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    cv2.imshow('mask', mask)
    # cv2.waitKey(0)

    # usuniecie zle wykrytych pojdynczych pikseli
    kernel = np.ones((6, 6), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)

    # cv2.imshow('obrazek', erosion)
    # cv2.waitKey(0)

    dilation = cv2.dilate(erosion, kernel, iterations=1)

    # cv2.imshow('obrazek', dilation)
    # cv2.waitKey(0)

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
    if len(list_of_points) != 12:
        print("Nie ma 12 punktow")
        return None

    else:

        # print(list_of_points)
        list_of_corners = find_corners(list_of_points)

        if len(list_of_corners) != 4:
            print('Lista rogow')
            print(list_of_corners)
            print('Lista puntkow')
            print(list_of_points)
            return None

        list_of_corners.reverse()
        # print('1. ' + str(list_of_points))

        checked_list_of_points = check_vertex_list(list_of_corners)
        # print('2. ' + str(checked_list_of_points))
        increased_list_of_points = increase_board_area(checked_list_of_points)

        pts1 = np.float32([increased_list_of_points[0], increased_list_of_points[1], increased_list_of_points[2],
                           increased_list_of_points[3]])

        pts2 = np.float32([[0, 0], [600, 0], [600, 600], [0, 600]])

        # stworzenie macierzy tranformacji perspektywicznej
        M = cv2.getPerspectiveTransform(pts1, pts2)

        # transformacja perspektywiczna
        dst = cv2.warpPerspective(source_image, M, (600, 600))

        # cv2.imshow("obrazek", dst)
        # cv2.waitKey()

        return dst


def find_checkers(image):
    # dodanie rozmycia zeby lepiej wykrywac kola
    blurred_img = cv2.medianBlur(image, 7)
    gray_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1, 40, param1=37, param2=22, minRadius=29,
                               maxRadius=40)  # 1,40,35,22,25,35

    if circles is not None:
        circles = np.uint16(np.around(circles))
        index = 1

        img_circles = image.copy()

        for i in circles[0, :]:
            # print(str(index) + ': ' + str(i))
            index += 1
            # draw the outer circle
            cv2.circle(img_circles, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(img_circles, (i[0], i[1]), 2, (0, 0, 255), 3)

        cv2.imshow('obrazek', img_circles)
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

    # print(squares_coord)
    # for i in squares_coord:
    #     cv2.rectangle(img, (i[0][0], i[0][1]), (i[1][0], i[1][1]), (122, 240, 122), 4)
    #
    # cv2.imshow('image', img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    return squares_coord


def find_colored_checkers(image, checkers, squares):
    lower_white = np.array([0, 0, 200])  # 0,0,20   5,100,100
    upper_white = np.array([180, 255, 255])  # 180,50,255  25,255,255

    # zamiana na HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # cv2.imshow('image', hsv)

    # stworzenie obrazu binarnego z pikseli z podanego zakresu
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # cv2.imshow('image', mask)
    # cv2.waitKey()


    # # usuniecie zle wykrytych pojdynczych pikseli
    kernel = np.ones((30, 30), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=1)

    # cv2.imshow('image', dilation)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    board_set = ['n'] * 64

    # print(checkers)
    # print(squares)

    for checker in checkers:
        x1 = checker[0] - 15
        y1 = checker[1] - 15

        x2 = checker[0] + 15
        y2 = checker[1] + 15

        crop_img = dilation[y1:y2, x1:x2]
        height, width = crop_img.shape
        if height == 0 or width == 0:
            return None

        n_non_zero = cv2.countNonZero(crop_img)
        position = -1

        if (n_non_zero / (height * width)) > 0.8:
            color = 'WM'
        else:
            color = 'BM'

        for idx, square in enumerate(squares):
            if (checker[0] > square[0][0]) and (checker[0] < square[1][0]) \
                    and (checker[1] > square[0][1]) and (checker[1] < square[1][1]):
                position = idx
                break

        board_set[position] = color

    return board_set


def run_all(img):
    img_transformed = board_perspective_transform(img)
    if img_transformed is not None:
        checkers_list = find_checkers(img_transformed)
        if checkers_list is not None:
            squares_coordinates = find_board_squares()

            mojatablic = find_colored_checkers(img_transformed, checkers_list[0], squares_coordinates)

            # print(len(mojatablic))
            # index = 0
            # for x in mojatablic:
            #     if index == 7:
            #         print(x)
            #         index = -1
            #     else:
            #         print(x + '  ', end='')
            #
            #     index += 1

            # cv2.imshow('obrazek', img_transformed)

            return mojatablic, img_transformed

        else:
            print("nie ma kolke")

            return None, None
    else:
        print("nie 4 pkt")
        return None, None


def check_if_was_move(source, list_of_eight_after_source):
    cnt = 0
    for x in list_of_eight_after_source:
        if x == source:
            cnt += 1

    if cnt > 5:
       return True
    else:
        return False


cap = cv2.VideoCapture(4)
# fgbg = cv2.createBackgroundSubtractorMOG2()

move_counter = 0
counter = 0
avoid_first_frame = 1
prev = []
list_of_eight_prev = []


while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        tab, img = run_all(frame)
        cv2.imshow('frame', frame)
        if tab is not None and img is not None:
            cv2.imshow('lol', img)
            if avoid_first_frame == 1:

                prev = tab
                avoid_first_frame += 1

            else:
                if prev != tab:
                    if counter == 0:
                        prev = tab
                        counter += 1
                    else:
                        list_of_eight_prev.append(tab)
                        counter += 1
                else:
                    if counter > 0:
                        list_of_eight_prev.append(tab)
                        counter += 1

            if counter == 8:
                if check_if_was_move(prev, list_of_eight_prev):
                    move_counter += 1
                    print(str(move_counter) + '------------------------RUCH--------------------------------------------------------------')
                    counter = 0
                    list_of_eight_prev = []
                    prev = tab
                else:
                    counter = 0
                    list_of_eight_prev = []
                    prev = tab

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
