# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:07:06 2018

@author: MSI
"""

import numpy as np, math

#All itu true kalo semua nilainya true
#All berlaku buat array 1D
#np.all() berlaku buat array 2D atau lebih
# all values true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))
print("================")

#Any itu true jika ada satu nilai aja true
#Any berlaku buat array 1D
#np.any() berlaku buat array 2D atau lebih
l = [1, 3, 4, 0]
print(any(l))

l = [0, False]
print(any(l))

l = [0, False, 5]
print(any(l))

l = []
print(any(l))
print("================")

coba = [1,1,1,1,1]
coba1 = np.array([1,0,0,0,0])
coba2 = np.array([[1,0,0],[0,0,1]])
print(all(coba1))
print(any(coba1))
print(all(coba2[0]))
print(any(coba2[0]))
if any(coba1): print("Betul")

a = [1, 2, 3, 4, 5]
b = [1, 2, 4]

print(all(i in a for i in b)) # Checks if all items are in the list
print(any(i in a for i in b)) # Checks if any item is in the list

print("=== List Comprehension ===")
squares = [x**2 for x in range(10)]
coba2 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(squares)
print(coba2)

#Hasil 1
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
print(len(matrix), len(matrix[0]))

#Hasil 2
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print (transposed) #--> hasil 2 == hasil 1

img = [100,200,100,200]
temp = []
for element in img:
    if element < 127:
        temp.append(0)
    else:
        temp.append(255)
img = temp
print(img)

img1 = np.array([
       [0,0,1,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,1,1,1],
       [0,0,1,1,1,1],
       [0,0,1,1,0,1],
       [1,1,1,1,1,1],
       [1,1,1,1,1,1],
       [1,1,1,1,1,1]])
img2 = [
       [0,0,1,0,0, 0],
       [0,0,0,0,0, 0],
       [0,0,0,1,1, 1],
       [0,0,1,1,1, 1],
       [0,0,1,1,0, 1]]
w = len(img1)
h = len(img1[0])
#temp = []
temp = img1[1:h, 1:w]
temp1 = img1[1:w, 1:h-1]
temp2 = img1[0:w-2, 0:h-3]
print(w,h)            
print(temp)
print(temp1)
print(temp2)
print("=========")
se = np.ones((3,3), np.uint8)
for i in range(w):
    for j in range(h):
        if i+2 < w and j+2 < h:
            print(img1[i:i+len(se), j:j+len(se)])
            print(np.all(img1[i:i+len(se), j:j+len(se)]))
            print(np.any(img1[i:i+len(se), j:j+len(se)]))
    print("\n")
print(math.floor(len(se)/2))
print(np.pad(img1, (2,2), "constant"))

print("=== Operasi Matriks ===")
matriks1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriks2 = np.array([[7,8,9],[4,5,6],[1,2,3]])
print(matriks1+matriks2)
print(matriks1*matriks2)
print(matriks1*matriks2)
