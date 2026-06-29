# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:50:46 2018

@author: MSI
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

lena = cv2.imread("../Dataset/lena.png")
lenaGray = cv2.imread("../Dataset/lena.png", cv2.IMREAD_GRAYSCALE)

#=== Ambil BGR ===
blue = lena[:,:,0]
green = lena[:,:,1]
red = lena[:,:,2]

#=== Flip Gambar ===
lenaFlip = np.fliplr(lena)

#=== Gabung Gambar ===
lenaConcat = np.hstack((lena, lenaFlip))

cv2.imshow('Lena RGB', lena)
cv2.imshow('Lena Gray', lenaGray)
cv2.imshow('Red', red)
cv2.imshow('Green', green)
cv2.imshow('Blue', blue)
cv2.imshow('Flipped', lenaFlip)
cv2.imshow('Concat', lenaConcat)

#=== Ambil Shape, Width, dan Height ===
rgbShape = lena.shape
grayShape = lenaGray.shape
width, height = lena.shape[:2]

print (rgbShape)
print (grayShape)
print (width)
print (height)

cv2.waitKey(0)
cv2.destroyAllWindows()