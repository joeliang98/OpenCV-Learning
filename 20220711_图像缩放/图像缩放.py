# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 22:45:06 2022

@author: joeBridge

import cv2
a = cv2.imread(r"E:\Python\OpenCV\OpenCV Learning\real_gray_image_469_528.jpg")
b = cv2.resize(a,(200,100))
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.waitKey()
cv2.destroyAllWindows()


import cv2
a = cv2.imread(r"E:\Python\OpenCV\OpenCV Learning\real_gray_image_469_528.jpg")
size = (200,100)
b = cv2.resize(a,size)
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.waitKey()
cv2.destroyAllWindows()

import cv2
a = cv2.imread(r"E:\Python\OpenCV\OpenCV Learning\real_gray_image_469_528.jpg")
rows,cols,chn = a.shape
size = (round(cols*0.5),round(rows*1.5))
b = cv2.resize(a,size)
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.waitKey()
cv2.destroyAllWindows()
"""
import cv2
a = cv2.imread(r"E:\Python\OpenCV\OpenCV Learning\real_gray_image_469_528.jpg")

b = cv2.resize(a,None,fx=0.5,fy=1.3)
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.waitKey()
cv2.destroyAllWindows()
