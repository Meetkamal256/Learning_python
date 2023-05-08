#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0:
        return new_list
    elif idx > len(new_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list


#
# def replace_in_list(my_list, idx, element):
#     if 0 <= idx < len(my_list):
#         my_list[idx] = element
#     return my_list


def main():
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 99
    new_list = replace_in_list(my_list, idx, new_element)
    print(new_list)
    print(my_list)


main()
