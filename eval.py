# -*- coding: utf-8 -*-
import cv2 as cv
## TODO: Допишите импорт библиотек, которые собираетесь использовать

def predict_box(image):

    blur = cv.blur(image, (3, 3))

    R = cv.inRange(blur, (0, 0, 150), (180, 150, 255))
    BL = cv.inRange(blur, (90, 0, 0), (255, 110, 110))
    BD = cv.inRange(blur, (210, 0, 0), (255, 170, 170))
    B = cv.inRange(blur, (170, 0, 0), (255, 130, 130))

    #R_dil = cv.dilate(binarR, (5, 5), iterations=1)
    #BL_dil = cv.dilate(binarBL, (5, 5), iterations=1)
    #BD_dil = cv.dilate(binarBD, (5, 5), iterations=1)

    contoursR, hierarchy = cv.findContours(R, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contoursB, hierarchy = cv.findContours(B, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contoursBL, hierarchy = cv.findContours(BL, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contoursBD, hierarchy = cv.findContours(BD, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    min_area = 200
    filtered_contours = []
    for contour in contoursR:
        area = cv.contourArea(contour)
        if area > min_area:
            filtered_contours.append(contour)

    for contour in contoursB:
        area = cv.contourArea(contour)
        if area > min_area:
            filtered_contours.append(contour)
            
    for contour in contoursBL:
        area = cv.contourArea(contour)
        if area > min_area:
            filtered_contours.append(contour)

    for contour in contoursBD:
        area = cv.contourArea(contour)
        if area > min_area:
            filtered_contours.append(contour)

    if filtered_contours:
        largest_contour = max(filtered_contours, key=cv.contourArea)
        x, y, w, h = cv.boundingRect(largest_contour)
                
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        box = (x, y, x+w, y+h)

        print(box)
        return box
    else:
        box = (0, 0, 0, 0)

        print(box)
        return box