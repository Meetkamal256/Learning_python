#!/usr/bin/python3
# a function that deletes the item at a specific position in a list.
def delete_at(my_list=[], idx=0):
    if idx > len(my_list):
        return my_list
    elif idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list


def main():
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)


main()
