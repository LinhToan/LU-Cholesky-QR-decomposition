# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:54:32 2020

@author: Hiro
"""

"""
This program will use LU decomposition to solve Ax=b.
"""

import numpy as np # import the numpy library

A = np.array([[1, 2, 3], [2, -1, 1], [3, 0, -1]]) # creates an A matrix

b = np.array([9, 8, 3]) # creates a b vector

L, U = LU_decomposition(A) # decomposes A into L and U matrices

m = len(A) # the number of rows of A

x = np.zeros(b.size) # creates an x matrix
y = np.zeros(b.size) # creates a y matrix

def LUsolver(A, b):
    # forward substitution to solve Ly = b
    for i in range(0, m, 1):
        y[i] = b[i] / L[i][i]
        for j in range(0, i, 1):
            y[i] -= y[k] * L[i][j]
    # back substitution to solve Ux = y
    for i in range(n-1, -1, -1):
        x[i] = y[i] / U[i][i]
        for j in range(i-1, -1, -1):
            U[i] -= x[i] * U[i][j]
    return x