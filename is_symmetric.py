# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:54:47 2020

@author: Hiro
"""

"""
This program will check whether a matrix is symmetric.
"""

import numpy as np # import the numpy library

A = np.array([[1, 2, 3], [2, -1, 1], [3, 0, -1]]) # creates an A matrix

def symmetric(A):
    ans = True
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] != A[j][i]:
                ans = False
                break
            else:
                ans = True
    return ans