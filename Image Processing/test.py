# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:13:05 2018

@author: MSI
"""

import numpy as np
import math
import cv2
import numpy_indexed as npi
#import pcd

a = np.array([[0, 4, 4, 2],
              [1, 3, 0, 2],
              [3, 2, 4, 4]])
b = np.array([[6, 9, 8, 6],
              [7, 7, 9, 6],
              [8, 6, 5, 7]])

c = np.where(a < 3, 0, 1)
print(c)
d = np.where(a >= 3, 1, 0)
print(d)

e = np.array([0,1,2,3,4,5,6])
for i in range(0,10,4):
    print(i)

q, w = 9, 5
q-=1
print(1 == 1.0)

dc = {'rendang':'padang', 'rawon':'malang', 'seblak':'bandung'}

m = np.array([
     [1, 275],
     [1, 441],
     [1, 494],
     [1, 593],
     [2, 679],
     [2, 533],
     [2, 686],
     [3, 559],
     [3, 219],
     [3, 455],
     [4, 605],
     [4, 468],
     [4, 692],
     [4, 613]])
arr = npi.group_by(m[:, 0]).split(m[:, 1])
print(list(dc.keys())[list(dc.values()).index('malang')])