"""inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """initialize a private instance attribute
        Args:
            width - represents width of rectangle
            height - represents height of rectangle"""
        self.__width = width
        self.__height = height

        self.integer_validator('width', width)
        self.integer_validator('height', height)
        
    def area(self):
        return self.__width * self.__height
    
    def __str__(self):
        """returns the print() and str() representation of a Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    
# def main():
#     r = Rectangle(3, 5)

#     print(r)
#     print(r.area())
    
# main()
        
        
