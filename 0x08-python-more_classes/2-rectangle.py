class Rectangle:
    """class constructor"""
    def __init__(self, width=0, height=0):
        """initialize private instance attributes
        Args:
            width - represents width of rectangle
            height - represents height of rectangle
        Raises:
            TypeError - when height is not an integer
             ValueError: when height is < 0"""
        self.__width = width
        self.__height = height

    """getter for width"""
    @property
    def width(self):
        return self.__width

    """setter for width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """getter for height"""
    @property
    def height(self):
        return self.__height

    """setter for height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """calculates area of rectangle
        returns: width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of rectangle
            returns: 2(width + height)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)


my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))





