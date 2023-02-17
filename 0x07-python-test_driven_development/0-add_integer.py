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
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
