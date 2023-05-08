"""inherits from class rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """define a new class square"""

    def __init__(self, size):
        """intialize a private instance attribute
        Args:
            size - represents size of the square
        raise:
            TypeError - if size is not an integer
            ValueError - if size is <= 0
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculates area of square"""
        return self.__size * self.__size


s = Square(13)

print(s)
print(s.area())
