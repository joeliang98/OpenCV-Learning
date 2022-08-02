# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:02:38 2022

@author: joeBridge
"""

import cv2
a = cv2.imread(r"E:\Python\OpenCV\OpenCV Learning\image_469_528.jpg")
b = cv2.flip(a,0)
c = cv2.flip(a,5)
d = cv2.flip(a,-1)
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)
cv2.imshow("d",d)

cv2.waitKey()
cv2.destroyAllWindows()





