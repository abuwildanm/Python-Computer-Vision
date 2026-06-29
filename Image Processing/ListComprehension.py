# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:57:27 2018

@author: MSI
"""

import numpy as np

#=== Loop dan List Comprehension ===
# Sintaks : [<the_expression> for <the_element> in <the_iterable>]
# Sintaks di atas sama dengan sintaks ini :
# for <the_element> in <the_iterable>:
#     <the_expression>
print("=== List Comprehension (sederhana) ===")
multiples = []
for n in range(1,10):
    multiples.append(n*5)
print("Pake for:\n", multiples)

multiples = [n*5 for n in range(1,10)]
print("Pake compre:\n", multiples)

#=== Kondisi dalam List Comprehension ===
# Sintaks (jika if saja) : [<the_expression> for <the_element> in <the_iterable> if <the_condition>]
# Sintaks (jika if else) : [<the_expression> if <the_condition> else <other_expression> for <the_element> in <the_iterable>]
# Sintaks di atas sama dengan sintaks ini :
#for <the_element> in <the_iterable>:
#    if <the_condition>:
#        <the_expression>
#    else:
#        <other_expression>

print("\n=== List Comprehension (if) ===")
evens = []
for n in range(1,10):
    if n%2 == 0:
        evens.append(n)
print("Pake for:\n", evens)

evens = [n for n in range(1,10) if n%2 == 0]
print("Pake compre:\n", evens)

print("\n=== List Comprehension (if-else) ===")
pangkat = []
for n in range(1,10):
    if n%2 == 0:
        pangkat.append(n**2)
    else:
        pangkat.append(n**3)
print("Pake for:\n", pangkat)

pangkat = [n**2 if n%2 == 0 else n**3 for n in range(1,10)]
print("Pake compre:\n", pangkat)

#=== List Comprehension dalam Loop Bersarang ===
# Sintaks : [ <the_expression> for <element_a> in <iterable_a> (optional if <condition_a>)
#                              for <element_b> in <iterable_b> (optional if <condition_b>)
#                              for <element_c> in <iterable_c> (optional if <condition_c>)
#                              ... and so on ...]
# Sintaks di atas sama dengan sintaks ini :
#for <element_a> in <iterable_a>:
#    for <element_b> in <iterable_b>:
#        <the_expression>
print("\n=== List Comprehension (nested loop) ===")
perkalian = []
for n in range(1,4):
    for m in range(1,10):
        perkalian.append(n*m)
print("Pake for:\n", perkalian)

perkalian = [n*m for n in range(1,4) for m in range(1,10)]
print("Pake compre:\n", perkalian)

print("\n=== List Comprehension (nested loop matrix) ===")
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
flatten = []
for row in matrix:
    for element in row:
        flatten.append(element)
print("Pake for:\n", flatten)

flatten = [element for row in matrix for element in row]
print("Pake compre:\n", flatten)

#=== Nested List Comprehension (list compre di dalam list compre) ===
# Sintaks : [[<the_expression> for <element_dalam> in <iterable_dalam>] for <element_luar> in <iterable_luar>]
# Sintaks di atas sama dengan sintaks ini :
#for <element_luar> in <iterable_luar>:
#    for <element_dalam> in <iterable_dalam>:
#        <the_expression>
print("\n=== Nested List Comprehension ===")
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
transpose = []
for i in range(len(matrix[0])):
    temp = []
    print("Tahap ke-", i)
    for row in matrix:
        temp.append(row[i])
        print(temp)
    transpose.append(temp)
print("Pake for:\n", transpose)

transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Pake compre:\n", transpose)

#=== Latihan Percobaan ===
print("\n=== Latihan Percobaan ===")
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
jumlah = 0
for row in matrix:
    for element in row:
        jumlah += element
print("Pake for:\n", jumlah)

jumlah = [0 + element for row in matrix for element in row]
print("Pake compre:\n", jumlah)