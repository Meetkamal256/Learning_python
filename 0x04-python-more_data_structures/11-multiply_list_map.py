def multiply_list_map(my_list=[], number=0):
    """a function that returns a list with all values multiplied by a number without using any loops."""
    return list(map(lambda x: x * number, my_list))


def main():
    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)


main()
