#!/usr/bin/python3
""" pascal triangle function """


def pascal_triangle(n):
    """ Represent Pascal's Triangle of size n. """
    if n <= 0:
        return []

    triangl = [[1]]
    while len(triangl) != n:
        tris = triangl[-1]
        tmp = [1]
        for i in range(len(tris) - 1):
            tmp.append(tris[i] + tris[i + 1])
        tmp.append(1)
        triangl.append(tmp)
    return triangl
