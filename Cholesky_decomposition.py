# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:53:50 2020

@author: Hiro
"""

def cholesky(A):
    """Performs a Cholesky decomposition of A, which must 
    be a symmetric and positive definite matrix. The function
    returns the lower variant triangular matrix, L."""
    
    from math import sqrt
    
    n = len(A)

    # Create zero matrix for L
    L = np.zeros(np.shape(A))

    # Perform the Cholesky decomposition
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k)) #this is the sum that appears in both formulas
            
            if i == k: # Diagonal elements
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                # Off diagonal elements
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
                
    return L