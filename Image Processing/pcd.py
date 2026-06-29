# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 11:15:59 2018

@author: MSI
"""

import numpy as np
import math
import copy

def rgbToGrayLuminosity(img):
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]
    gray = 0.21*R + 0.71*G + 0.07*B
    return gray

def rgbToGrayAverage(img):
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]
    gray = (R+G+B) / 3
    return gray

def rgbToGrayLightness(img):
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]
    gray = (np.maximum(R,G,B) + np.minimum(R,G,B)) / 2
    return gray

def imgNegative(img):
    neg = 255 - img
    return neg

def logtrans(img, c):
#    #cara 1
#    logtrans = copy.copy(Dataset)
#    for x in range (Dataset.shape[0]):
#        for y in range(Dataset.shape[1]):
#            logtrans[x][y] = c * (1 + np.log(Dataset[x][y]))
    
    #cara 2
    logtrans = c * np.log(1 + img)
    return logtrans

def powerlaw (img, c , gamma):
#    #cara 1
#    powerlaw = copy.copy(Dataset)
#    for x in range (Dataset.shape[0]):
#        for y in range(Dataset.shape[1]):
#            powerlaw[x][y] = c * (np.power(Dataset[x][y],gamma))
#    
#    #cara 2
#    powerlaw = c * np.power(Dataset,gamma)
    
    #cara 3
    powerlaw = c * (img**gamma)
    return powerlaw

def pieceWise(im):
    out_img = copy.copy(im)
    for i in range(0, im.shape[0]):
    	for j in range(0, im.shape[1]):
    		if im[i,j] <= 110:
    			out_img[i,j] = 0
    		elif im[i,j] <= 146:
    			out_img[i,j] = im[i,j]
    		else:
    			out_img[i,j] = 255
    return out_img

def bpSlicing(img):
    bps_8 = copy.copy(img)
    bps_7 = copy.copy(img)
    bps_6 = copy.copy(img)
    bps_5 = copy.copy(img)
    bps_4 = copy.copy(img)
    bps_3 = copy.copy(img)
    bps_2 = copy.copy(img)
    bps_1 = copy.copy(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[0]):
            bps_1 [i][j] = img[i][j] & 1
            bps_2 [i][j] = img[i][j] & 2
            bps_3 [i][j] = img[i][j] & 4
            bps_4 [i][j] = img[i][j] & 8
            bps_5 [i][j] = img[i][j] & 16
            bps_6 [i][j] = img[i][j] & 32
            bps_7 [i][j] = img[i][j] & 64
            bps_8 [i][j] = img[i][j] & 128
    
    arr = [bps_1, bps_2, bps_3, bps_4, bps_5, bps_6, bps_7, bps_8]
    return arr

def substraction(img, substractor):
    img1 = copy.copy(img)
    img1 = img - substractor
    return img1

def andOperation(img):
    width, height = img.shape
    mask = copy.copy(img)
    for i in range(height):
        for j in range(width):
            mask[:width, :height] = 0
            mask[200:300, 200:300] = 255
        
    hasil = copy.copy(img)
    for i in range(height):
        for j in range(width):
            #hasil[i][j] = min(Dataset[i][j], mask[i][j])
            hasil[i][j] = img[i][j] & mask[i][j]
    
    return hasil

def orOperation(img):
    width, height = img.shape
    mask = copy.copy(img)
    for i in range(height):
        for j in range(width):
            mask[:width, :height] = 0
            mask[200:300, 200:300] = 255
        
    hasil = copy.copy(img)
    for i in range(height):
        for j in range(width):
            #hasil[i][j] = max(Dataset[i][j], mask[i][j])
            hasil[i][j] = img[i][j] | mask[i][j]
    
    return hasil

def xorOperation(img):
    width, height = img.shape
    mask = copy.copy(img)
    for i in range(height):
        for j in range(width):
            mask[:width, :height] = 0
            mask[200:300, 200:300] = 255
        
    hasil = copy.copy(img)
    for i in range(height):
        for j in range(width):
            hasil[i][j] = img[i][j] ^ mask[i][j]
    
    return hasil

def imgToBinary(img, threshold, inverse=False):
    result = np.copy(img)
    height, width = result.shape
    for i in range(height):
        for j in range(width):
            if not inverse:
                if result[i, j] < threshold:
                    result[i][j] = 0
                else:
                    result[i][j] = 255
            else:
                if result[i, j] >= threshold:
                    result[i][j] = 0
                else:
                    result[i][j] = 255

#    result = np.where(Dataset >= threshold, 255, 0)
    return result

def averageBlur(img, sizeKernel):
    kernel = np.ones(sizeKernel, np.uint8) / 9
    padding = math.floor(len(kernel)/2)
    
    #nambah padding (pinggiran)
    imgBesar = np.pad(img, (padding,padding), "constant")
    
    height, width = imgBesar.shape
    result = np.zeros(imgBesar.shape, np.uint8)
    
    #proses konvolusi lowpass filter (belum bisa dinamis ukuran kernel)
    for i in range(1, height-1):
        for j in range(1, width-1):
            hasilKali = kernel * imgBesar[i-1:i+2, j-1:j+2]
            result[i,j] = round(np.sum(hasilKali))
            # result[i,j] = np.sum(hasilKali)
    
    #motong padding(pinggiran)
    result = result[1:height-1, 1:width-1]
    
    return result

def dilation(imgBinary, sizeKernel):
    kernel = np.ones(sizeKernel, np.uint8)
    padding = math.floor(len(kernel)/2)
    
    #binary Dataset -> 0 1 Dataset
    binary = imgBinary / 255
    
    #nambah padding (pinggiran)
    binaryBesar = np.pad(binary, (padding,padding), "constant")
    
    height, width = binaryBesar.shape
    result = np.zeros(binaryBesar.shape, np.uint8)
    
    #proses dilasi
    for i in range(1, height-1):
        for j in range(1, width-1):
            if np.any(binaryBesar[i-1:i+2, j-1:j+2]):
                result[i,j] = 1
    
    #motong padding(pinggiran)
    result = result[1:height-1, 1:width-1]
    
    #0 1 Dataset -> binary Dataset
    result = result * 255
    return result

def erotion(imgBinary, sizeKernel):
    kernel = np.ones(sizeKernel, np.uint8)
    padding = math.floor(len(kernel)/2)
    
    #binary Dataset -> 0 1 Dataset
    binary = imgBinary / 255
    
    #nambah padding (pinggiran)
    binaryBesar = np.pad(binary, (padding,padding), "constant")
    
    height, width = binaryBesar.shape
    result = np.zeros(binaryBesar.shape, np.uint8)
    
    #proses erosi
    for i in range(1, height-1):
        for j in range(1, width-1):
            if np.all(binaryBesar[i-1:i+2, j-1:j+2]):
                result[i,j] = 1
    
    #motong padding(pinggiran)
    result = result[1:height-1, 1:width-1]
    
    #0 1 Dataset -> binary Dataset
    result = result * 255
    return result

def opening(imgBinary, sizeKernel):
    result = np.copy(imgBinary)
    result = erotion(result, sizeKernel)
    result = dilation(result, sizeKernel)
    return result

def closing(imgBinary, sizeKernel):
    result = np.copy(imgBinary)
    result = dilation(result, sizeKernel)
    result = erotion(result, sizeKernel)
    return result

def segmentation(imgBinary, sizeKernel):
    kernel = np.ones(sizeKernel, np.uint8) * -1
    padding = math.floor(len(kernel)/2)
    kernel[padding, padding] = 8
    
    #binary Dataset -> 0 1 Dataset
    binary = imgBinary / 255
    
    #nambah padding (pinggiran)
    binaryBesar = np.pad(binary, (padding,padding), "constant")
    
    height, width = binaryBesar.shape
    result = np.zeros(binaryBesar.shape, np.uint8)
    
    #proses segmentasi
    for i in range(1, height-1):
        for j in range(1, width-1):
            hasilKali = kernel * binaryBesar[i-1:i+2, j-1:j+2]
            result[i,j] = np.sum(hasilKali)
    
    #motong padding(pinggiran)
    result = result[1:height-1, 1:width-1]
    
    #0 1 Dataset -> binary Dataset
#    result = result * 255
#    result = np.where(result != 0, result * 255, 0)
    return result

def findStart(binSeg):
    for i in range(0, binSeg.shape[0]):
        for j in range(0, binSeg.shape[1]):
            if (binSeg[i,j] == 1):
                return [i,j]
                
#4 direction
def representation(imgSeg):
    #binary Dataset -> 0 1 Dataset
#    binary = imgToBinary()
    binary = imgSeg / 255
#    print(binary, np.max(binary))
    
#    height, width = binary.shape
    result = []
    path = []
    start = findStart(binary)
    i, j = start[0], start[1]
    while(True):
        if(binary[i, j+1] == 1 and [i,j+1] not in path):
            result.append(0)
            j += 1
            path.append([i,j])
            
        elif(binary[i-1, j] == 1 and [i-1,j] not in path):
            result.append(1)
            i -= 1
            path.append([i,j])
            
        elif(binary[i, j-1] == 1 and [i,j-1] not in path):
            result.append(2)
            j -= 1
            path.append([i,j])
            
        elif(binary[i+1, j] == 1 and [i+1,j] not in path):
            result.append(3)
            i += 1
            path.append([i,j])
        
        if ([i,j] == start):
            break
        
    return result

#8 direction
def representation8(imgSeg):
    #binary Dataset -> 0 1 Dataset
#    binary = imgToBinary()
    binary = imgSeg / 255
    
#    height, width = binary.shape
    result = []
    path = []
    start = findStart(binary)
    i, j = start[0], start[1]+1
    while([i,j] != start):
        if(binary[i, j+1] == 1 and [i,j+1] not in path):
            result.append(0)
            j += 1
            path.append([i,j])
            
        elif(binary[i-1, j+1] == 1 and [i-1,j+1] not in path):
            result.append(1)
            i -= 1
            j += 1
            path.append([i,j])
            
        elif(binary[i-1, j] == 1 and [i-1,j] not in path):
            result.append(2)
            i -= 1
            path.append([i,j])
            
        elif(binary[i-1, j-1] == 1 and [i-1,j-1] not in path):
            result.append(3)
            i -= 1
            j -= 1
            path.append([i,j])
            
        elif(binary[i, j-1] == 1 and [i,j-1] not in path):
            result.append(4)
            i -= 1
            path.append([i,j])
            
        elif(binary[i+1, j-1] == 1 and [i+1,j-1] not in path):
            result.append(5)
            i += 1
            j -= 1
            path.append([i,j])
            
        elif(binary[i+1, j] == 1 and [i+1,j] not in path):
            result.append(6)
            i += 1
            path.append([i,j])
            
        elif(binary[i+1, j+1] == 1 and [i+1,j+1] not in path):
            result.append(7)
            i += 1
            j += 1
            path.append([i,j])
    
    print(path)
    print(result)
    return result


































