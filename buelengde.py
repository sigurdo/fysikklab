# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:25:21 2019

@author: Sigurd
"""

import numpy as np

def getI(buelengde, x_interp, y_interp, alpha):
    s = 0
    i = 0
    while s < buelengde:
        i += 1
        s += np.sqrt((x_interp[i]-x_interp[i-1])**2 + (y_interp[i]-y_interp[i-1])**2)
    
    return i

#print(getI(0.22, x_interp, y_interp, alpha))