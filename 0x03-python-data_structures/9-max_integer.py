#!/usr/bin/python3
# a function that finds the biggest integer of a list.
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_num = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max_num:
            max_num = my_list[i]
    return max_num


def main():
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))


main()
