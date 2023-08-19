#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    mult = 0
    mult2 = 0
    for i in range(len(my_list)):
        for j in range(len(my_list[i]) - 1):
            mult += my_list[i][j] * my_list[i][j+1]
        mult2 += my_list[i][1]
    avrg = mult / mult2
    return (avrg)
