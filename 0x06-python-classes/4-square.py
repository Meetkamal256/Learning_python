class Square:
    """define a class Square"""

    def __init__(self, size=0):
        """initializes a private instance attribute"""

        """Args:
            size - size of the square
        Raise:
            TypeError - if size is not an integer
            ValueError - if size is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates area of square"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size is not an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


def main():
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
