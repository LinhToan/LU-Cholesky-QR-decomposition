# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:55:05 2020

@author: Hiro
"""

"""
This program will determine the definiteness of a matrix.
"""

from numpy.linalg import eig, eigvals, eigh, eigvalsh

u = eigvals(A)
ans = ' '

def definite(A):
    for i in range(len(u)):
        if u[i] >= 0:
            if u[i] == 0:
                ans = 'The matrix is positive semi-definite'
            else:
                ans = 'The matrix is positive definite.'
        elif u[i] <= 0:
            if u[i] == 0:
                ans = 'The matrix is negative semi-definite.'
            else:
                ans = 'The matrix is negative definite.'
        else:
            ans = 'The matrix is indefinite.'
    return ans