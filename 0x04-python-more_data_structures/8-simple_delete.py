def simple_delete(a_dictionary, key=""):
    """ a function that deletes a key in a dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary


def main():
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

def print_sorted_dictionary(a_dictionary):
    """a function that prints a dictionary by ordered keys"""
    for keys, values in sorted(a_dictionary.items()):
        print("{}: {}".format(keys, values))


main()