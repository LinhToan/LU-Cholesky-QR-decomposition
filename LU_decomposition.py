# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:53:14 2020

@author: Hiro
"""

def LU_decomposition(A):
    """Perform LU decomposition of a square matrix (numpy array) using the Doolittle factorization."""
    #import numpy 
    import numpy as np
    
    #make sure type is correct (or you could set this up to try and convert the type instead of raising an error.)
    if type(A) != np.ndarray:
        raise TypeError('Input must be a numpy array, type {} will not work'.format(type(A)))
    
    #check dimension to ensure A is square
    if np.shape(A)[0] != np.shape(A)[1]:
        raise ValueError('Input matrix is not square, shape {} will not work'.format(np.shape(A)))

    L = np.zeros_like(A, dtype=float)
    U = np.zeros_like(A, dtype=float)
    N = np.size(A, 0)

    for k in range(N):
        L[k, k] = 1
        U[k, k] = A[k, k] - np.dot(L[k, :k], U[:k, k]) 
        for j in range(k+1, N):
            U[k, j] = A[k, j] - np.dot(L[k, :k], U[:k, j])
        for i in range(k+1, N):
            L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]

    return L, U