#!/usr/bin/python3
""" define a matrix multiplication fucntion """


def matrix_mul(m_a, m_b):
    """  function that multiplies 2 matrices
    Args:
        m_a (matrice): input matrice
        m_b (matrice): input matrice
    Returns:
        new matrice (m_a * m_b)
    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: if m_a or m_b is not a list of lists
        ValueError: if m_a or m_b is empty (it means: = [] or = [[]])
        TypeError: if one element of those list of lists is not
        an integer or a float
        TypeError: if m_a or m_b is not a rectangle
        ValueError: If m_a and m_b can’t be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(x, list) for x in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(x, list) for x in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(elem, (int, float)) for elem in
               [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for elem in
               [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    invert_b = []
    for x in range(len(m_b[0])):
        new_row = []
        for y in range(len(m_b)):
            new_row.append(m_b[y][x])
        invert_b.append(new_row)

    new = []
    for row in m_a:
        new_row = []
        for col in invert_b:
            mul = 0
            for i in range(len(invert_b[0])):
                mul += row[i] * col[i]
            new_row.append(mul)
        new.append(new_row)
    return(new)
