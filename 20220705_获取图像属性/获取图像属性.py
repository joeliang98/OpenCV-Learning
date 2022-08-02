# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 21:51:04 2022

@author: joeBridge
"""
import cv2
a = cv2.imread(r"E:\Python\OpenCV-Learning\OpenCV Learning\gray_image.jpg",cv2.IMREAD_UNCHANGED)
b = cv2.imread(r"E:\Python\OpenCV-Learning\OpenCV Learning\image.jpg",cv2.IMREAD_UNCHANGED)
print(a.shape)
print(a.shape)

print(a.size) #size = row*column*channel
print(b.size)

print(a.dtype)
print(b.dtype)