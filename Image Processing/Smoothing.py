# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:07:48 2018

@author: MSI
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2, pcd

# read image
img = cv2.imread("../Dataset/dna.jpg")

# rgb to gray
gray = cv2.imread("../Dataset/dna.jpg", cv2.IMREAD_GRAYSCALE)

# proses smoothing
average = cv2.blur(gray, (3,3))
gauss = cv2.GaussianBlur(gray, (3,3), 0)
median = cv2.medianBlur(gray, 3)

images = [img, gray, average, gauss, median]
titles = ["Original", "Gray", "Averaging", "Gaussian", "Median"]

# menampilkan image
for i in range(len(images)):
    cv2.imshow(titles[i], images[i])
    
# waktu tunggu hasil
# angka 0 artinya waktu tunggu hasilnya infinite sehingga dia akan nutup kalo ditekan tombol (tombol bebas)
# jika angka 0 diganti angka 100 misalnya, maka waktu delay hasilnya adalah 100 ms
cv2.waitKey(0)

# The function destroyAllWindows destroys all of the opened HighGUI windows.
cv2.destroyAllWindows()