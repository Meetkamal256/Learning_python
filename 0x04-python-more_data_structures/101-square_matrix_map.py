def square_matrix_map(matrix=[]):
    """a function that computes the square value of all integers of a matrix using map"""

    def row(x):
        return x**x

    return list(map(row, matrix))


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    new_matrix = square_matrix_map(matrix)
    print(new_matrix)
    print(matrix)


main()
