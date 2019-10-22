# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:25:21 2019

@author: Sigurd
"""

import numpy as np

def getIndex(buelengde, x_interp, y_interp, alpha):
    s = 0
    i = 0
    while s < buelengde and i < len(x_interp) - 1:
        sNew = s + np.sqrt((x_interp[i+1]-x_interp[i])**2 + (y_interp[i+1]-y_interp[i])**2)
        if abs(sNew - buelengde) < abs(s - buelengde):
            i += 1
            s = sNew
        else:
            break
    
    return i

