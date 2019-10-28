import numpy as np
import math as math 

def standardavvik(v_list):
    avg = np.mean(v_list)
    sum = 0
    for val in v_list:
        a=val-avg
        b = a**2
        sum+=b
    N = len(v_list)
    dx = math.sqrt(float(sum)/(float(N-1))) 
    return dx

def standardfeil(v_list):
    length = len(v_list)
    avv = standardavvik(v_list)
    avg_avv = float(avv)/(float(math.sqrt(length)))
    return avg_avv 
    


        




