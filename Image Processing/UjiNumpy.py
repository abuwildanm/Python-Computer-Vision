# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 20:17:39 2018

@author: MSI
"""

import numpy as np

a = np.array([[1,1,0,0,0],
              [1,1,0,1,0],
              [0,0,1,1,0],
              [0,0,0,1,0],
              [0,0,0,1,0]])

b = np.array([[1,1,1,1,1],
              [1,1,1,1,1],
              [1,1,1,1,1],
              [0,1,1,1,0],
              [0,0,0,0,0]])

c = np.array([[1,2],
              [3,4]])

d= np.array([[5,6],
             [7,8]])

e = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20],
              [21,22,23,24,25]])

eBesar = np.pad(e, (1,1), "constant")
kernel = np.ones((3,3)) / 10
result = np.zeros(eBesar.shape)

print("Asli\n", e)
print("Besar\n", eBesar)
print("Kernel\n", kernel)

#h, w = e.shape
#for i in range(1, h-1):
#    for j in range(1, w-1):
##        if len(a[i-1:i+2, j-1:j+2][0]) == 2:
#            print(e[i-1:i+2, j-1:j+2], i, j)
#            print(e[i,j])
#            print("-----------------------")

h, w = eBesar.shape
for i in range(1, h-1):
    for j in range(1, w-1):
        kali = kernel * eBesar[i-1:i+2, j-1:j+2]
        result[i,j] = np.sum(kali)

print("Hasil\n", result)
print("Hasil Bulat\n", np.round(result))
result = result[1:h-1, 1:w-1]
print("Hasil\n", result)
