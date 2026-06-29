# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:40:37 2018

@author: MSI
"""

#%matplotlib inline
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
# from skimage import data

photo_data = misc.imread("../Dataset/lena.png")

# === Average Method ====
#x,y,z=photo_data.shape ## where z is the RGB dimension
### Method block begin 
#photo_data[:] = photo_data.mean(axis=-1,keepdims=1) 
### Method Block ends 
#plt.figure(figsize=(10,20))

# === Luminosity Method ===
#W = [0.2,0.5,0.3] # weights
#W_mean = np.tensordot(photo_data,W, axes=((-1,-1)))[...,None]
#photo_data[:] = W_mean.astype(photo_data.dtype)

# === Lightness Method ===
photo_data[:] = np.max(photo_data,axis=-1,keepdims=1)/2+np.min(photo_data,axis=-1,keepdims=1)/2

plt.imshow(photo_data)
plt.show()