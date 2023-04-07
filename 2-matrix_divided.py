#!/usr/bin/python3

''' function that perfoms matrix division'''


def matrix_divided(matrix, div):
    '''
    divide all elements of a matrix

    Params:
        matrix: mtrx list of lists of any type (int or float)
        div: divisor (integer or float)

    Raises:
        TypeError: if matrix doesn't have integers or floats
        TypeError: if rows are not equal in size
        TypeError: if div is not an integer or float
        ValueError: if div is 0

    Returns:
        New matrix after division
    '''

    if (
            not isinstance(matrix, list)
            or matrix == []
            or not all(isinstance(row, list) for row in matrix)
            or not all(
                isinstance(item, (int, float))
                for row in matrix
                for item in row
            )
        ):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])        
