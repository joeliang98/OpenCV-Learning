# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 22:05:46 2022

@author: joeBridge
"""


import cv2
import numpy as np
a = cv2.imread("E:\Python\OpenCV-Learning\OpenCV Learning\image.jpg")
b = np.ones((101,101,3)) #100rows 100columns 3channels
b = a[220:400,250:350]
a[0:180,0:100] = b
cv2.imshow("original",a)
cv2.imshow("face",b)
cv2.waitKey()
cv2.destroyAllWindows()
