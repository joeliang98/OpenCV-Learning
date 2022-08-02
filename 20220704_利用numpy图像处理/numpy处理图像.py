# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:13:48 2022

@author: joeBridge
"""

'''
import cv2
import numpy as np
i = cv2.imread(r"E:\Python\OpenCV\OpenCV Learning\gray_image.jpg",cv2.IMREAD_UNCHANGED)
print(i.item(100,100))
numX = 0
numY = 0
while numX < 200:
    while numY < 200:
        i.itemset((numX,numY),0)
        numY+=1
    numY = 0
    numX += 1
print(i.item(100,100))

cv2.imshow("demo",i)
cv2.waitKey(0)
'''

import cv2
import numpy as np
i = cv2.imread(r"E:\Python\OpenCV\OpenCV Learning\BVB.jpg",cv2.IMREAD_UNCHANGED)
print(i.item(100,100,0))
i.itemset((100,100,0),255)
print(i.item(100,100,0))

