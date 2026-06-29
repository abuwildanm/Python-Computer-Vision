# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:50:24 2018

@author: MSI
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import pcd

# read image
img = cv2.imread("Dataset/train/apel1.png")
gray = cv2.imread("Dataset/train/apel1.png", cv2.IMREAD_GRAYSCALE)

blur = pcd.averageBlur(gray, (3,3))
#binary1 = pcd.imgToBinary(blur, 200)
binary = pcd.imgToBinary(blur, 200, True)
seg = pcd.segmentation(binary[1:binary.shape[0]-1, 1:binary.shape[1]-1], (3,3))
# rep = pcd.representation(seg)
#rep1 = pcd.represent_4_direction(seg)

print(blur)
#print(binary1)
#print(binary)
#print(seg)
# print(rep)
#print(seg.shape)
#print(seg.shape[0])
#print(seg.shape[1])

images = [gray, binary, seg]
titles = ["Gray", "Binary", "Segmentation"]

# menampilkan image
for i in range(len(images)):
    cv2.imshow(titles[i], images[i])
    
cv2.waitKey(0)
cv2.destroyAllWindows()