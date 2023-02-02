#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """a function that computes the square value of all integers of a matrix."""
    return [list(map(lambda x: x ** 2, row)) for row in matrix]


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)


main()