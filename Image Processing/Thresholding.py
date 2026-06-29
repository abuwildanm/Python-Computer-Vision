# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:58:02 2018

@author: MSI
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

# read image
img = cv2.imread("../Dataset/pool.png")

# rgb to gray
gray = cv2.imread("../Dataset/pool.png", cv2.IMREAD_GRAYSCALE)

# gray to binary
ret,binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
ret,binaryInv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
ret,trunc = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
ret,tozero = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
ret,tozeroInv = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
ret,otsu = cv2.threshold(gray, 50, 255, cv2.THRESH_OTSU)

images = [img, gray, binary, binaryInv, trunc, tozero, tozeroInv, otsu]
titles = ["Original", "Gray", "Binary", "Binary Inv", "Trunc", "Tozero", "Tozero Inv", "Otsu"]

# menampilkan image
for i in range(len(images)):
    cv2.imshow(titles[i], images[i])

# waktu tunggu hasil, jika dikasi 0 nanti program tidak akan langsung ke close, dia baru close ketika ditekan stop
cv2.waitKey(0)

# memhapus semua data semacam cache tp bukan cache
cv2.destroyAllWindows()