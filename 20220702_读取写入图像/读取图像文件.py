# -*- coding: utf-8 -*-

import cv2
i = cv2.imread("E:\\Python\\OpenCV\\OpenCV Learning\\image.jpg")
cv2.imshow("demo",i)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("E:\\Python\\OpenCV\\OpenCV Learning\\image.jpg",i)

