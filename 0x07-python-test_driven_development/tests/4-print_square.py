#!/usr/bin/python3
"""a function that prints a square with the character # """


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")


# print_square(4)
# print("")
# print_square(10)
# print("")
# print_square(0)
# print("")
# print_square(1)
# print("")
# try:
#     print_square(-1)
# except Exception as e:
#     print(e)
# print("")
# try:
#     print_square()
# except Exception as e:
#     print(e)
# print("")
# try:
#     print_square(6, 9)
# except Exception as e:
#     print(e)
# print("")
