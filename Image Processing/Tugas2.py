# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 12:38:33 2018

@author: MSI
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

# read image
img = cv2.imread("../Dataset/koin.jpg")

# rgb to gray
gray = cv2.imread("../Dataset/koin.jpg", cv2.IMREAD_GRAYSCALE)

# menghilangkan noise
blur = cv2.blur(gray, (3,3))

# gray to binary
ret,binary = cv2.threshold(blur, 95, 255, cv2.THRESH_BINARY)

# Kernel 3x3 isi  1 1 1 ...
kernel = np.ones((3,3), np.uint8)
ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

# proses morfologi
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel) # erosi -> dilasi
erosi = cv2.erode(opening, kernel, iterations = 1)
erosi1 = cv2.erode(erosi, kernel, iterations = 1)
erosi2 = cv2.erode(erosi1, kernel, iterations = 1)

images = [img, gray, binary, opening, erosi, erosi1, erosi2]
titles = ["Original", "Gray", "Binary", "Hasil 1", "Hasil 2", "Hasil 3", "Hasil 4", "Hasil 5"]

# menampilkan image
for i in range(len(images)):
    cv2.imshow(titles[i], images[i])
    
# waktu tunggu hasil
# angka 0 artinya waktu tunggu hasilnya infinite sehingga dia akan nutup kalo ditekan tombol (tombol bebas)
# jika angka 0 diganti angka 100 misalnya, maka waktu delay hasilnya adalah 100 ms
cv2.waitKey(0)

# The function destroyAllWindows destroys all of the opened HighGUI windows.
cv2.destroyAllWindows()