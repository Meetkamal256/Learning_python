class Square:
    """a class that represents a square"""

    def __init__(self, size):
        """initializing square class
        args: size - represents the size of the square defined"""

        self.__size = size


def main():
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)


main()
