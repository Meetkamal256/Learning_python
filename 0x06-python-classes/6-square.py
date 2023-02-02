class Square:
    """Generates a square but still building
                    builds an instance with a known size
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a private instance attribute
        Args:
            size (any): The size of a square is crucial for a square,
            many things depend on it, area computation, etc.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2 or \
                not isinstance(position[0], int) or \
                not isinstance(position[1], int) \
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """returns the area of the square
        Returns:
                        int: the square of the size
        """
        return self.__size ** 2

    @property
    def size(self):
        """returns the size of the square
        Returns:
            int: the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method that returns to the current the square area of the object
        Args:
            value (int): the value to set the size
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """returns the position of the square
        Returns:
            int: _description_
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not isinstance(value[0], int) or \
                not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = valuetouch




my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
