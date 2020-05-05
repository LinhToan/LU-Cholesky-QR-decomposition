# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:55:20 2020

@author: Hiro
"""

"""
This program handles exceptions for the Cholesky factorization function above
"""

def exHandle(A):
    if symmetric(A) == True and definite(A) == 'The matrix is positive definite.':
        return cholesky(A)
    elif symmetric(A) == True and definite(A) != 'The matrix is positive definite.':
        ans = 'This matrix is not positive definite.'
    elif definite(A) != 'The matrix is positive definite.' and symmetric(A) != True:
        ans = 'This matrix is not symmetric.'
    else:
        ans = 'This matrix is neither positive definite nor symmetric.'
    return ans