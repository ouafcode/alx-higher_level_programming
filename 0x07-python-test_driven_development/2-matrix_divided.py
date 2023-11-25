#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ functions that divides all elements of a matrix
    Args:
        matrix (list of list) : input matrix
        div (int) : input number
    Returns:
        return new matrix
    Raises:
        TypeError: if matrix is not list of list of integers/floats
        TypeError: if row of the matrix doesn't have the same size
        ZeroDivisionError: if div is equal to 0
    """
    if(not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(x, list) for x in matrix) or
        not all(isinstance(elem, (int, float))
                for elem in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round((elem / div), 2) for elem in x] for x in matrix]
    return(new)
