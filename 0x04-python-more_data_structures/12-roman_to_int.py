#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return (0)

    r_nbr = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    N = len(roman_string)
    i = N-1
    while i >= 0:
        if i < N - 1 and r_nbr[roman_string[i]] < r_nbr[roman_string[i + 1]]:
            res -= r_nbr[roman_string[i]]
        else:
            res += r_nbr[roman_string[i]]
        i -= 1
    return (res)
