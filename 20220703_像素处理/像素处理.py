# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 14:25:23 2022

@author: joeBridge
"""
import cv2
i = cv2.imread("E:\Python\OpenCV-Learning\OpenCV Learning\\BVB.jpg",cv2.IMREAD_UNCHANGED)
'''
p = i[100,100]
print(p)
i[100,100,0] = 255
p = i[100,100]
print(p)
cv2.imshow("demo",i)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
cv2.imshow("original",i)
i[100:150,100:150] = [255,255,255]
cv2.imshow("result",i)
cv2.waitKey(0)
cv2.destroyAllWindows()


