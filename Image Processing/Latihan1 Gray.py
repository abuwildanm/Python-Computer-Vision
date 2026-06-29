# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 11:25:24 2018

@author: MSI
"""

import numpy as np
import matplotlib.pyplot as plt
import pcd

img = plt.imread("../Dataset/lena.png")

imgGray = pcd.rgbToGrayLuminosity(img)
imgGray1 = pcd.rgbToGrayAverage(img)
imgGray2 = pcd.rgbToGrayLightness(img)

#img1 = Image.open('Dataset/lena.png').convert('LA') #make PIL

plt.imshow(img), plt.title("Original")
plt.show()
plt.imshow(imgGray, cmap = 'gray'), plt.title("Luminosity Method")
plt.show()
plt.imshow(imgGray1, cmap = plt.get_cmap('gray')), plt.title("Average Method")
plt.show()
plt.imshow(imgGray2, cmap = 'gray'), plt.title("Lightness Method")
plt.show()