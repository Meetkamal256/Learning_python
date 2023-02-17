#!/usr/bin/python3
"""this module has one function that adds up two integers"""

def add_integer(a, b=98):
    """returns the sum of two integers or floats as integers
    Args:
        a: first argument
        b: second argument
        
    Returns:
        sum of the two arguments
    
    Raises:
        TypeError: if either of the arguments is not an integer or a float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


# print(add_integer(1, 2))
# print(add_integer(100, -2))
# print(add_integer(2))
# print(add_integer(100.3, -2))
# try:
#     print(add_integer(4, "School"))
# except Exception as e:
#     print(e)
# try:
#     print(add_integer(None))
# except Exception as e:
#     print(e)
    
# try:
#     print(add_integer())
# except Exception as e:
#     print(e)

# try:
#     print(add_integer(a, 12))
# except Exception as e:
#     print(e)
# try:
#     print(add_integer("a", "b"))
# except Exception as e:
#     print(e)
# try:
#     print(add_integer(5, "hard"))
# except Exception as e:
#     print(e)
