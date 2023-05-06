#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in reversed(my_list):
        print("{}".format(i))


def main():
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)


main()
