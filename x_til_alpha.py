
def from_x_to_alpha(x,x_list):
    diff_0 = abs(x_list[0]-x)
    x_1 = 0
    for num in range(1,len(x_list)):
        diff = abs(x_list[num]-x)
        if (diff < diff_0):
            diff_0 = diff 
            x_1 = num 
    return x_1
