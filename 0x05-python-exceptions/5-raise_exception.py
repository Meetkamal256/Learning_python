def raise_exception():
    """a function that raises a type exception."""
    raise TypeError


def main():
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")


main()
