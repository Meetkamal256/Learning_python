"""inherits from rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """initialize a private instance attribute"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    # def area(self):
    #     """calculates area of square"""
    #     return self.__size * self.__size

    def __str__(self) -> str:
        return "[Square] {}/{}".format(self.__size, self.__size)


s = Square(13)

print(s)
print(s.area())
