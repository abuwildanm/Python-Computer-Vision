# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 05:58:03 2018

@author: MSI
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import pcd

img = cv2.imread("../Dataset/koin.jpg")
gray = cv2.imread("../Dataset/koin.jpg", cv2.IMREAD_GRAYSCALE)

blur = pcd.averageBlur(gray, (3,3))
binary = pcd.imgToBinary(blur, 95)
#kernel = np.ones((3,3), np.uint8)
opening = pcd.opening(binary, (3,3))
erosi = pcd.erotion(opening, (3,3))
erosi1 = pcd.erotion(erosi, (3,3))
erosi2 = pcd.erotion(erosi1, (3,3))

cv2.imshow("gray", gray)
cv2.imshow("blur", blur)
cv2.imshow("binary", binary)
cv2.imshow("opening", opening)
cv2.imshow("erosi", erosi)
cv2.imshow("erosi1", erosi1)
cv2.imshow("erosi2", erosi2)

cv2.waitKey(0)
cv2.destroyAllWindows()