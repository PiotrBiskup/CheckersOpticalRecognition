import numpy as np
import cv2

# green = np.uint8([[[233, 249, 255]]])
# hsvGreen = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# print(hsvGreen)
# lowerLimit = (hsvGreen[0][0][0]-10,100,100)
# upperLimit = (hsvGreen[0][0][0]+10,255,255)
# print(upperLimit)
# print(lowerLimit)

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

def find_colored_checkers(image, checkers, squares):

    board_set = ['n'] * 64

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    kernel = np.ones((30, 30), np.uint8)
    kernel_color = np.ones((6, 6), np.uint8)

    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    erosion_white = cv2.erode(mask_white, kernel, iterations=1)
    dilation_white = cv2.dilate(erosion_white, kernel, iterations=1)

    mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)
    erosion_pink = cv2.erode(mask_pink, kernel_color, iterations=1)
    dilation_pink = cv2.dilate(erosion_pink, kernel, iterations=1)

    mask_green = cv2.inRange(hsv, lower_dark_green, upper_dark_green)
    erosion_green = cv2.erode(mask_green, kernel_color, iterations=1)
    dilation_green = cv2.dilate(erosion_green, kernel, iterations=1)

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

        if (n_non_zero_w / (height_w * width_w)) > 0.8:
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
