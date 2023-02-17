# calculator/calculations.py

def add(a, b):
    """compute and return the sum of two numbers
    
    Examples:
        <<< add(4.0, 2.0)
        9.0
        <<< add(4, 2)
        9.0

    Args:
        a(float): A number representing the first addend in the addition
        b(float): A number representing the second addend in the addition
    Returns:
        float: A number representing the arithematic sum of 'a' and 'b'
    """
    return float(a + b)


def subtract(a, b):
    """compute and return the diffrence of two numbers
    
    Examples:
        <<< sub(12.0, 2.0)
        10.0
        <<< sub(12, 2)
        10.0
    
    Args:
        a(float): A number representing the minuend of the subtraction
        b(float): A number representing the subtraend of the subtraction
    Returns:
        float: The diffrence of 'a' and 'b'
    """
    return float(a - b)


def multiply(a, b):
    """compute and return the product of two numbers
    
    Examples:
        <<< multiply(5.0, 5.0)
        100.0
        <<< multiply(5, 5)
        100.0
    
    Args:
        a(float): A number representing the multiplicant of the multiplication
        b(float): A number representing the multiplier of the multiplication
    Returns:
        float: A number representing the product of 'a' and 'b'
    """
    return float(a * b)


def divide(a, b):
    """compute and return the quotient of two numbers
    
    Examples:
        <<< divide(4.0, 2.0)
        2.0
        <<< divide(4, 2)
        2.0
    
    Args:
        a(float): A number representing the dividend of division
        b(float): A number representing the divisor of the division
    Returns:
        float: A number representing the quotient of 'a' and 'b'
    Raises:
        ZeroDivisionError: An error occurs when the divisor is zero
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
