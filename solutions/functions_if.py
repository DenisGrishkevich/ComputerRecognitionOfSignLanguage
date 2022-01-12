#To simplify the work, create for the array with coordinates x and y
#We also introduce variables that determine the maximum and minimum coordinates on each of the axes
def sign_if(p_list):
    p_list_x = []
    p_list_y = []
    for i in range(0, 21):
        p_list_x.append(p_list[i][0])
        p_list_y.append(p_list[i][1])
    max_x = max(p_list_x)
    max_y = max(p_list_y)
    min_x = min(p_list_x)
    min_y = min(p_list_y)
    

    # A sign
    p_list_x_a = p_list_x.copy()
    p_list_x_a.pop(3)
    p_list_x_a.pop(2)
    max_x_a = max(p_list_x_a)
    if p_list_x[4] == max_x_a and p_list_y[4] == min_y:
        return "a"
    
    # B sign
    if (p_list_y[5] > p_list_y[6] and p_list_y[6] > p_list_y[7] and p_list_y[7] > p_list_y[8]) and (p_list_y[9] > p_list_y[10] and p_list_y[10] > p_list_y[11] and p_list_y[11] > p_list_y[12]) and (p_list_y[13] > p_list_y[14] and p_list_y[14] > p_list_y[15] and p_list_y[15] > p_list_y[16]) and (p_list_y[17] > p_list_y[18] and p_list_y[18] > p_list_y[19] and p_list_y[19] > p_list_y[20]):
                return "b"
            
    # C sign
    if (p_list_x[5] and p_list_x[9] and p_list_x[13] and p_list_x[17]) < p_list_x[20] and (p_list_y[5] and p_list_y[9] and p_list_y[13] and p_list_y[17]) > p_list_y[20] and (p_list_x[17] < p_list_x[18] and p_list_x[18] < p_list_x[19] and p_list_x[19] < p_list_x[20]) and (p_list_x[13] < p_list_x[14] and p_list_x[14] < p_list_x[15] and p_list_x[15] < p_list_x[16]):
        if p_list_y[4] * 1.7 > p_list_y[20] and (p_list_x[1] < p_list_x[2] and p_list_x[2] < p_list_x[3] and p_list_x[3] < p_list_x[4] and p_list_x[0] < p_list_x[17]):
            return "c"
        
    # D sign
    if (p_list_y[5] > p_list_y[6] and p_list_y[6] > p_list_y[7] and p_list_y[7] > p_list_y[8]) and p_list_y[8] == min_y and (p_list_x[2] > p_list_x[3] and p_list_x[3] > p_list_x[4]) and p_list_x[8] < p_list_x[2]:
        return "d"
    
    # E sign 
    if (p_list_y[20] and p_list_y[12]) < p_list_y[4] and p_list_x[20] < p_list_x[4] and p_list_x[4] < p_list_x[12] and p_list_y[20] > p_list_y[19] and p_list_y[6] < p_list_y[7] and p_list_y[10] < p_list_y[11] and p_list_y[14] < p_list_y[15] and p_list_x[5] > p_list_x[10]:
        return "e"
    
    # F sign
    if (p_list_y[5] > p_list_y[6] and p_list_y[6] < p_list_y[7] and p_list_y[7] < p_list_y[8]) and (p_list_y[9] > p_list_y[10] and p_list_y[10] > p_list_y[11] and p_list_y[11] > p_list_y[12]) and (p_list_y[13] > p_list_y[14] and p_list_y[14] > p_list_y[15] and p_list_y[15] > p_list_y[16]) and (p_list_y[17] > p_list_y[18] and p_list_y[18] > p_list_y[19] and p_list_y[19] > p_list_y[20] and p_list_y[0] > p_list_y[17]):
        return "f"
    
    # G sign
    if (p_list_y[8] < p_list_y[10] and p_list_x[8] > p_list_x[10] and p_list_y[4] > p_list_y[10] and p_list_x[4] > p_list_x[10] and (p_list_x[5] < p_list_x[6] and p_list_x[6] < p_list_x[7] and p_list_x[7] < p_list_x[8]) and p_list_x[8] > p_list_x[3] and p_list_x[0] < p_list_x[17]):
        return "g"
    
    # H sign
    if (p_list_x[8] < p_list_x[12] and p_list_y[8] < p_list_y[12] and p_list_x[12] == max_x and (p_list_x[5] < p_list_x[6] and p_list_x[6] < p_list_x[7] and p_list_x[7] < p_list_x[8]) and (p_list_x[9] < p_list_x[10] and p_list_x[11] < p_list_x[12]) and p_list_y[12] * 1.5 < p_list_y[8] and p_list_x[13] < p_list_x[14] and p_list_x[14] > p_list_x[15] and p_list_x[15] > p_list_x[16]):
        return "h"
    
    # I sign
    if (p_list_y[20] == min_y and p_list_x[4] < p_list_x[2]):
        return "i"
    
    # J sign
    if ((p_list_y[20] == max_y or p_list_y[19] == max_y) and p_list_y[5] == min_y):
        return "j"
    
    # K sign
    if (p_list_y[4] > (p_list_y[8] and p_list_y[12]) and p_list_y[4] < (p_list_y[5] and p_list_y[9]) and p_list_x[4] > p_list_x[12] and p_list_x[4] < p_list_x[8]):
        return "k"
    
    # L sign
    if (p_list_x[4] == max_x and p_list_y[8] == min_y):
        return "l"
    
    # M sign
    if (p_list_x[4] < p_list_x[14] and p_list_x[4] > p_list_x[17] and (p_list_y[6] < p_list_y[7] and p_list_y[7] < p_list_y[8])):
        return "m"
    
    # N sign
    if (p_list_x[4] < p_list_x[10] and p_list_x[4] > p_list_x[13] and (p_list_y[6] < p_list_y[7] and p_list_y[7] < p_list_y[8]) and p_list_y[14] > p_list_y[4]):
        return "n"
    
    # O sign
    if (p_list_x[5] and p_list_x[9] and p_list_x[13] and p_list_x[17]) < p_list_x[20] and (p_list_y[5] and p_list_y[9] and p_list_y[13] and p_list_y[17]) > p_list_y[20] and (p_list_x[17] < p_list_x[18] and p_list_x[18] < p_list_x[19] and p_list_x[19] < p_list_x[20]) and (p_list_x[13] < p_list_x[14] and p_list_x[14] < p_list_x[15] and p_list_x[15] < p_list_x[16]):
        if p_list_y[4] * 1.7 < p_list_y[20] and (p_list_x[1] < p_list_x[2] and p_list_x[2] < p_list_x[3]):
            return "o"
        
    # P sign
    if (p_list_x[4] > (p_list_x[5] and p_list_x[17]) and p_list_x[4] < (p_list_x[8] and p_list_x[12]) and p_list_y[4] < p_list_y[17] and p_list_y[4] > p_list_y[5] and p_list_x[0] < p_list_x[17]):
        return "p"
    
    # Q sign
    if (p_list_y[4] == max_y and p_list_x[8] == max_x):
        return "q"
    
    # R sign
    if (p_list_x[12] > p_list_x[8] and (p_list_y[5] > p_list_y[6] and p_list_y[6] > p_list_y[7] and p_list_y[7] > p_list_y[8]) and (p_list_y[9] > p_list_y[10] and p_list_y[10] > p_list_y[11] and p_list_y[11] > p_list_y[12])):
        return "r"
    
    # S sign
    if (p_list_y[20] and p_list_y[12]) > p_list_y[4] and p_list_x[20] < p_list_x[4] and p_list_x[4] < p_list_x[8] and p_list_y[20] > p_list_y[19] and p_list_y[4] > p_list_y[14] and p_list_y[8] > p_list_y[7]:
        return "s"
    
    # T sign
    if (p_list_x[4] < p_list_x[6] and p_list_x[4] > p_list_x[10] and p_list_y[4] < p_list_y[9]):
        return "t"
    
    # U sign
    if ((p_list_y[5] > p_list_y[6] and p_list_y[6] > p_list_y[7] and p_list_y[7] > p_list_y[8]) and (p_list_y[9] > p_list_y[10] and p_list_y[10] > p_list_y[11] and p_list_y[11] > p_list_y[12]) and p_list_y[14] < p_list_y[15]):
        if (abs(p_list_x[5] - p_list_x[9]) * 1.7 > abs(p_list_x[8] - p_list_x[12])):
            return "u"
    
    # V sign
    if ((p_list_y[5] > p_list_y[6] and p_list_y[6] > p_list_y[7] and p_list_y[7] > p_list_y[8]) and (p_list_y[9] > p_list_y[10] and p_list_y[10] > p_list_y[11] and p_list_y[11] > p_list_y[12]) and p_list_y[14] < p_list_y[15]):
        if (abs(p_list_x[5] - p_list_x[9]) * 1.7 < abs(p_list_x[8] - p_list_x[12])):
            return "v"
    
    # W sign
    if ((p_list_y[5] > p_list_y[6] and p_list_y[6] > p_list_y[7] and p_list_y[7] > p_list_y[8]) and (p_list_y[9] > p_list_y[10] and p_list_y[10] > p_list_y[11] and p_list_y[11] > p_list_y[12]) and (p_list_y[13] > p_list_y[14] and p_list_y[14] > p_list_y[15] and p_list_y[15] > p_list_y[16])):
        return "w"
    
    # X sign
    if (p_list_y[6] > p_list_y[7] and p_list_x[6] < p_list_x[7] and p_list_x[7] < p_list_x[8] and p_list_y[7] < p_list_y[8]):
        return "x"
    
    # Y sign
    if (p_list_y[20] == min_y and p_list_x[4] == max_x):
        return "y"
    
    # Z sign
    if (p_list_y[5] > p_list_y[6] and p_list_y[6] > p_list_y[7] and p_list_y[7] > p_list_y[8]) and p_list_y[8] == min_y and p_list_x[3] > p_list_x[4] and p_list_x[8] == max_x:
        return "z"
