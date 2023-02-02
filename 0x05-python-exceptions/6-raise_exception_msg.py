def raise_exception_msg(message=""):
    raise NameError(message)


def main():
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)


main()
