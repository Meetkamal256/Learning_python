#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ a function that replaces all occurrences of an element by another in a new list."""
    x = list(map(lambda x: replace if x == search else x, my_list))
    return x

#
# def search_replace(my_list, search, replace):
#     def find_search(element):
#         return element if element != search else replace
#     return list(map(find_search, my_list))


def main():
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)


main()
