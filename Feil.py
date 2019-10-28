import numpy as np

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
    len = len(v_list)
    avg_avv = float(avv)/(float(math.sqrt(len)))
    return avg_avv 
    


        




