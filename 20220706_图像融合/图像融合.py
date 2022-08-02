# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 23:39:40 2022

@author: joeBridge
"""

import cv2
a = cv2.imread("E:\Python\OpenCV-Learning\OpenCV Learning\BVB2.jpg")
b = cv2.imread("E:\Python\OpenCV-Learning\OpenCV Learning\image_469_528.jpg")
result = cv2.addWeighted(a,0.1,b,0.5,56)

cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("result",result)

cv2.waitKey()
cv2.destroyAllWindows()
