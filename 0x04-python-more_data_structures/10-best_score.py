#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    v_max = 0
    k_max = None
    for k, v in a_dictionary.items():
        if v > v_max:
            v_max = v
            k_max = k
    return (k_max)
