# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 22:56:39 2022

@author: joeBridge
"""
import cv2
import numpy as py
a = cv2.imread(r"E:\Python\OpenCV\OpenCV Learning\image.jpg")
b = a
add1 = a+b          #取模加法
add2=cv2.add(a,b)   #饱和计算
cv2.imshow("add1",add1)
cv2.imshow("add2",add2)
cv2.waitKey()
cv2.destroyAllWindows()