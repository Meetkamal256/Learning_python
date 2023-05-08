class Square:
    """defines a class Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__position = position
        self.__size = size

    def __int__(self, size=0):
        """initialize a private attribute size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates area of square"""
        """returns: square of size"""
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("Position must be a tuple of two positive integers")
        for i in value:
            if i < 0:
                raise TypeError("Position must be a tuple of two positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()

        # for i in range(self.__size):
        print(" " * self.__size, end="")
        for j in range(self.__size):
            print("#", end="")
        print()
        for j in range(self.__size):
            print("#", end="")
        print()
        for j in range(self.__size):
            print("#", end="")
        print()


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
