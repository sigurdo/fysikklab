import numpy as np
import math as math 

def standardavvik(v_list):
    avg = np.mean(v_list)
    sum = 0
    for val in v_list:
        a=val-avg
        sum+=a
    N = len(v_list)
    dx = math.sqrt(float(sum)/(float(N-1))) 
    return dx

def standardfeil(avv,v_list):
    length = len(v_list)
    avg_avv = float(avv)/(float(math.sqrt(length)))
    return avg_avv 
    


        




