# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:55:38 2020

@author: Hiro
"""

"""
This program will return the Gram-Schmidt orthonormal basis of a set of vectors.
"""

import numpy as np
from numpy.linalg import qr

def proj(u, a):
"""
This function calculates the projection of a onto u.
"""
    # projects v onto u
    return (np.dot(a,u) / np.dot(u,u)) * u

def gs(V):
    V = 1.0 * V
    U = np.copy(V)

    for i in xrange(1, V.shape[1]):
        for j in xrange(i):
            U[:,i] -= proj(U[:,j], V[:,i])

    # normalize column
    norm = (U ** 2).sum(axis = 0) ** 0.5
    E = U / norm
    return E