import numpy as np
from datasets.data_sign import *

alfabet = { 0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y", 25:"z"}

def distance_calc(p_list):
    sum_all = []
    p_list_all = scal_all(p_list)
    for j in range(0, 26):
        distance = []
        for i in range(0, 21):
            distance.append(np.sqrt((p_list_all[j][i][0] - zip_all[j][i][0])**2 + (p_list_all[j][i][1] - zip_all[j][i][1])**2 + (p_list_all[j][i][2] - zip_all[j][i][2])**2))
        sum_all.append(np.sum(distance))
    minimum_sum = min(range(len(sum_all)), key=sum_all.__getitem__)
    return alfabet[minimum_sum]

def scaling(sign, p_list):
    dxw = np.abs(sign[5][0] - sign[17][0])
    dyw = np.abs(sign[5][1] + sign[17][1])/2
    dxb = np.abs(p_list[5][0] - p_list[17][0])
    dyb = np.abs(p_list[5][1] + p_list[17][1])/2
    for i in range (1,21):
        p_list[i][0] * (dxw/dxb)
        p_list[i][1] * (dyw/dyb)
    return p_list
        
def scal_all(p_list):
    zip_p_list = []
    for i in range(0, 26):
        zip_p_list.append(scaling(zip_all[i], p_list))
    return zip_p_list

def check_correct(answer, answer_list, expected):
    if answer == expected:
        answer_list.append(100)
    else:
        answer_list.append(0)
        
def distance_calc_with(p_list):
    sum_all = []
    p_list_all = scal_all(p_list)
    for j in range(0, 26):
        distance = []
        for i in range(0, 21):
            distance.append(np.sqrt((p_list_all[j][i][0] - zip_all[j][i][0])**2 + (p_list_all[j][i][1] - zip_all[j][i][1])**2 + (p_list_all[j][i][2] - zip_all[j][i][2])**2))
        sum_all.append(np.sum(distance))
    minimum_sum = min(range(len(sum_all)), key=sum_all.__getitem__)
    answer = alfabet[minimum_sum]
    
    if answer == "a" or answer == "t" or answer == "n" or answer == "s" or answer == "m":
        if p_list_all[0][4][1] < p_list_all[0][18][1]:
            if p_list_all[0][4][0] > p_list_all[0][8][0]:
                return "a"
            if p_list_all[12][4][0] < p_list_all[12][14][0]:
                return "m"
            if p_list_all[13][4][0] < p_list_all[13][10][0]:
                return "n"
            if p_list_all[19][4][0] < p_list_all[19][6][0]:
                return "t"
        else:
            return "s"
        
    if answer == "c" or answer == "o":
        if p_list_all[2][4][1] * 1.7 > p_list_all[2][20][1]:
            return "c"
        else:
            return "o"
        
    if answer == "z" or answer == "d" or answer == "l":
        if p_list_all[3][19][1] < p_list_all[3][17][1]:
            return "d"
        if p_list_all[11][3][0] < p_list_all[11][4][0]:
            return "l"
        else:
            return "z"
        
    if answer == "r" or answer == "u" or answer == "k" or answer == "v" or answer == "w":
        if p_list_all[17][8][0] < p_list_all[17][12][0]:
            return "r"
        else:
            if p_list_all[10][4][1] < p_list_all[10][5][1]:
                return "k"
            if p_list_all[22][14][1] > p_list_all[22][15][1]:
                return "w"
            if p_list_all[20][8][0] < p_list_all[20][1][0]:
                return "u"
            else:
                return "v"
    
    if answer == "g" or answer == "p" or answer == "x":
        if p_list_all[15][4][0] < p_list_all[15][12][0]:
            return "p"
        else:
            if p_list_all[23][6][1] > p_list_all[23][7][1] and p_list_all[23][7][1] < p_list_all[23][8][1]:
                return "x"
            else:
                return "g"
            
    return answer

def saving_data_sign(p_list, number):
    if number < 100:
        np.save(f"datasets/neuro/sign_c/{number}.npy", p_list)
        return number+1