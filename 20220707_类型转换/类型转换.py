# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 21:44:54 2022

@author: joeBridge

import cv2
a = cv2.imread("E:\Python\OpenCV\OpenCV Learning\image_469_528.jpg")
b = cv2.cvtColor(a,cv2.COLOR_BGR2RGB)
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.waitKey()
cv2.destroyAllWindows()
"""

import cv2
#默认打开是三通道，所以第二个参数选取不改变
a = cv2.imread(r"E:\Python\OpenCV-Learning\OpenCV Learning\gray_image.jpg",cv2.IMREAD_UNCHANGED)
b = cv2.cvtColor(a,cv2.COLOR_GRAY2BGR)
cv2.imshow("a",a)
cv2.imshow("b",b)
print(a.shape)
print(b.shape)
bb,bg,br = cv2.split(b)
cv2.imshow("bb",bb)
cv2.imshow("bb",bg)
cv2.imshow("bb",br)
cv2.waitKey()
cv2.destroyAllWindows()

