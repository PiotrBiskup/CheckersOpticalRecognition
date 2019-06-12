import cv2
import numpy as np

lower_white = np.array([0, 0, 150])  # 0,0,200   5,100,100 , 0,0,200 - bardzo czule
upper_white = np.array([180, 50, 255])  # 180,50,255  25,255,255 - 180, 255, 255

lower_pink = np.array([160, 100, 100])
upper_pink = np.array([179, 255, 255])

lower_dark_green = np.array([50, 60, 60])
upper_dark_green = np.array([80, 255, 255])

lower_yellow = np.array([20, 100, 100])  # lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([100, 255, 255])  # upper_yellow = np.array([50, 255, 255])

lower_blue = np.array([74, 100, 100])  # 100,50,50  100, 70, 70     84,100,100
upper_blue = np.array([114, 255, 255])  # 130,255,255      104,255,255


def check_edges(hsv_image):
    mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    kernel_er = np.ones((6, 6), np.uint8)
    kernel_dil = np.ones((30, 30), np.uint8)
    erosion = cv2.erode(mask, kernel_er, iterations=1)
    dilation = cv2.dilate(erosion, kernel_dil, iterations=1)
    # cv2.imshow('zolete', dilation)
    # cv2.imshow('zoltemaksa', mask)

    image, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img2 = cv2.drawContours(image, contours, -1, (128, 255, 187), 3)

    list_of_edges_points = []

    for i in contours:
        cnt = i
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        img2 = cv2.line(img2, (cx, cy), (cx, cy), (128, 255, 187), 5)
        list_of_edges_points.append([cx, cy])

    if len(list_of_edges_points) == 8:
        return True
    else:
        return False


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

    #cv2.imshow('mask', mask)
    # cv2.waitKey(0)

    # usuniecie zle wykrytych pojdynczych pikseli
    kernel = np.ones((8, 8), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)

    #cv2.imshow('ed', erosion)
    # cv2.waitKey(0)

    dilation = cv2.dilate(erosion, kernel, iterations=1)

    # cv2.imshow('rogi', dilation)
    # cv2.waitKey(0)

    # znalezienie konturow
    image, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # rysowanie konturow
    img2 = cv2.drawContours(image, contours, -1, (128, 255, 187), 3)

    # wyliczenie srodkow masy prostokatow
    list_of_corners = []

    for i in contours:
        cnt = i
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        img2 = cv2.line(img2, (cx, cy), (cx, cy), (128, 255, 187), 5)
        list_of_corners.append([cx, cy])

    # cv2.imshow('obrazek', img2)
    # cv2.waitKey(0)

    if len(list_of_corners) != 4:
        print("Nie ma 4 rogow")
        return None

    else:

        if not check_edges(hsv):
            print('Nie ma 8 zoltych znacznikow')
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

    circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1, 40, param1=35, param2=25, minRadius=29,
                               maxRadius=45)  # 1,40,35,22,25,35

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

        small = cv2.resize(img_circles, (0, 0), fx=0.8, fy=0.8)
        cv2.imshow('Wykryte_pionki', small)
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

    board_set = ['n'] * 64

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    kernel = np.ones((12, 12), np.uint8)
    kernel_damka = np.ones((16, 16), np.uint8)
    kernel_color = np.ones((12, 12), np.uint8)

    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    erosion_white = cv2.erode(mask_white, kernel, iterations=1)
    dilation_white = cv2.dilate(erosion_white, kernel, iterations=1)

    # cv2.imshow('w', mask_white)

    mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)
    # erosion_pink = cv2.erode(mask_pink, kernel_color, iterations=1)
    dilation_pink = cv2.dilate(mask_pink, kernel_damka, iterations=1)

    # cv2.imshow('p', dilation_pink)

    mask_green = cv2.inRange(hsv, lower_dark_green, upper_dark_green)
    # erosion_green = cv2.erode(mask_green, kernel_color, iterations=1)
    dilation_green = cv2.dilate(mask_green, kernel_damka, iterations=1)

    # cv2.imshow('g', dilation_green)

    for checker in checkers:
        x1 = checker[0] - 15
        y1 = checker[1] - 15

        x2 = checker[0] + 15
        y2 = checker[1] + 15

        crop_img_w = dilation_white[y1:y2, x1:x2]
        height_w, width_w = crop_img_w.shape

        if height_w == 0 or width_w == 0:
            return None

        crop_img_p = dilation_pink[y1:y2, x1:x2]
        height_p, width_p = crop_img_p.shape

        if height_p == 0 or width_p == 0:
            return None

        crop_img_g = dilation_green[y1:y2, x1:x2]
        height_g, width_g = crop_img_g.shape

        if height_g == 0 or width_g == 0:
            return None

        n_non_zero_w = cv2.countNonZero(crop_img_w)
        n_non_zero_p = cv2.countNonZero(crop_img_p)
        n_non_zero_g = cv2.countNonZero(crop_img_g)

        if (n_non_zero_w / (height_w * width_w)) > 0.6:
            color = 'WM'
        elif (n_non_zero_p / (height_p * width_p)) > 0.6:
            color = 'WK'
        elif (n_non_zero_g / (height_g * width_g)) > 0.6:
            color = 'BK'
        else:
            color = 'BM'

        for idx, square in enumerate(squares):
            if (checker[0] > square[0][0]) and (checker[0] < square[1][0]) \
                    and (checker[1] > square[0][1]) and (checker[1] < square[1][1]):
                position = idx
                board_set[position] = color
                break

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
            print("There is no checkers")

            return None, None
    else:
        #nie znaleziono wszystkich znacznikow
        return None, None


# def check_if_was_move(source, list_of_eight_after_source):
#     cnt = 0
#     for x in list_of_eight_after_source:
#         if x == source:
#             cnt += 1
#
#     if cnt > 4:
#         return True
#     else:
#         return False


def choose_most_common_set(first_8_frames):

    amounts = []

    for x in first_8_frames:

        counter = 0

        for y in first_8_frames:

            if x == y:
                counter += 1

        amounts.append(counter)

    maximum = max(amounts)

    return first_8_frames[amounts.index(maximum)], maximum








# cap = cv2.VideoCapture(4)
#
# move_counter = 0
# counter = 0
# avoid_first_frame = 1
# prev = []
# list_of_eight_prev = []
#
# while cap.isOpened():
#     ret, frame = cap.read()
#
#     if ret:
#         tab, img_transf = run_all(frame)
#         # cv2.imshow('frame', frame)
#         if tab is not None and img_transf is not None:
#             # cv2.imshow('lol', img_transf)
#             if avoid_first_frame == 1:
#
#                 prev = tab
#                 avoid_first_frame += 1
#
#             else:
#                 if prev != tab:
#                     if counter == 0:
#                         prev = tab
#                         counter += 1
#                     else:
#                         list_of_eight_prev.append(tab)
#                         counter += 1
#                 else:
#                     if counter > 0:
#                         list_of_eight_prev.append(tab)
#                         counter += 1
#
#             if counter == 8:
#                 if check_if_was_move(prev, list_of_eight_prev):
#                     move_counter += 1
#                     print(str(move_counter) + '------------------------RUCH--------------------------------------------------------------')
#                     counter = 0
#                     list_of_eight_prev = []
#                     prev = tab
#                 else:
#                     counter = 0
#                     list_of_eight_prev = []
#                     prev = tab
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     else:
#         break
#
# cap.release()
# cv2.destroyAllWindows()
