import numpy as np
import matplotlib.pyplot as plt
import cv2
import pcd
import copy

img = cv2.imread("../Dataset/lena.png")
gray = cv2.imread("../Dataset/lena.png", cv2.IMREAD_GRAYSCALE)
gray1 = pcd.rgbToGrayAverage(img)

#Image Negative
neg = pcd.imgNegative(gray)

#Log Transformation
#Semakin kecil c semakin gelap, semakin besar c semakin terang
logTran = pcd.logtrans(gray, 15)

#Power-Law Transformation
powerLaw = pcd.powerlaw(gray1, 1, 4)

#Piecewise-Linear Transformation
piecewise = pcd.pieceWise(gray)

#Bit-plane Slicing
bps = pcd.bpSlicing(gray)

#Substraction
sub = pcd.substraction(img, 100)

#Operasi AND
andOp = pcd.andOperation(gray)

#Operasi OR
orOp = pcd.orOperation(gray)

#Operasi XOR
xorOp = pcd.xorOperation(gray)

plt.imshow(img), plt.title("Original")
plt.show()
plt.imshow(gray, cmap = 'gray'), plt.title("Gray")
plt.show()
plt.imshow(neg, cmap = 'gray'), plt.title("Image Negative")
plt.show()
plt.imshow(logTran, cmap = 'gray'), plt.title("Log Transformation")
plt.show()
plt.imshow(powerLaw, cmap = 'gray'), plt.title("Power-Law Transformation")
plt.show()
plt.imshow(piecewise, cmap = 'gray'), plt.title("Piecewise-Linear Transformation")
plt.show()
plt.imshow(bps[0], cmap = 'gray'), plt.title("1-bit")
plt.show()
plt.imshow(bps[1], cmap = 'gray'), plt.title("2-bit")
plt.show()
plt.imshow(bps[2], cmap = 'gray'), plt.title("3-bit")
plt.show()
plt.imshow(bps[3], cmap = 'gray'), plt.title("4-bit")
plt.show()
plt.imshow(bps[4], cmap = 'gray'), plt.title("5-bit")
plt.show()
plt.imshow(bps[5], cmap = 'gray'), plt.title("6-bit")
plt.show()
plt.imshow(bps[6], cmap = 'gray'), plt.title("7-bit")
plt.show()
plt.imshow(bps[7], cmap = 'gray'), plt.title("8-bit")
plt.show()
plt.imshow(sub, cmap = 'gray'), plt.title("Substraction")
plt.show()
plt.imshow(andOp, cmap = 'gray'), plt.title("Operasi AND")
plt.show()
plt.imshow(orOp, cmap = 'gray'), plt.title("Operasi OR")
plt.show()
plt.imshow(xorOp, cmap = 'gray'), plt.title("Operasi XOR")
plt.show()