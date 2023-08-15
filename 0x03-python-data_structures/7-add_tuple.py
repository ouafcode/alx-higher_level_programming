#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,0)
    elif len(tuple_b) < 2:
        tuple_b = tuple_b + (0,0)

    for i in range(1):
        new = (tuple_a[i] + tuple_b[i],
		tuple_a[i+1] + tuple_b[i+1])
    return (new)
