class Rectangle:
    """define a class rectangle"""
    def __init__(self, width, height):
        """initialize a private instance attribute
        Args:
            height - represent height of rectangle
            width - represent width of rectangle
        Raises:
                TypeError - when height or width is not an integer
                ValueError - when height or width is less than 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """calculates area of rectangle
        Returns: height * width"""
        return self.__height * self.__width

    def perimeter(self):
        """calculates perimeter of rectangle"""
        if self._width == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    # don"t understand from here yet
    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    # def __repr__(self):
    #     return f"Rectangle({self.__width}, {self.__height})"


my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))
