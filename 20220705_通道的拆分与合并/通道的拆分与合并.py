# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 22:33:41 2022

@author: joeBridge
"""

import cv2
import numpy as np
a = cv2.imread(r"E:\Python\OpenCV\OpenCV Learning\image.jpg")
'''
b,g,r = cv2.split(a)
cv2.imshow("original",a)
cv2.imshow("B",b)
cv2.imshow("G",g)
cv2.imshow("R",r)
m = cv2.merge([r,g,b])
cv2.imshow("merge",m)
'''
rows,cols,chn = a.shape
b = cv2.split(a)[1]
g = np.zeros((rows,cols),a.dtype)
r = np.zeros((rows,cols),a.dtype)
m = cv2.merge([b,g,r])
cv2.imshow("merge",m)
cv2.waitKey()
cv2.destroyAllWindows()
