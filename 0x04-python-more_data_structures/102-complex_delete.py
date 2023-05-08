def complex_delete(a_dictionary, value):
    """a function that deletes keys with a specific value in a dictionary."""
    keys_to_del = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys_to_del.append(key)
    for key in keys_to_del:
        del a_dictionary[key]
    return a_dictionary


def main():
    a_dictionary = {"lang": "C", "track": "Low", "pref": "C", "ids": [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, "C")
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, "c_is_fun")
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)


def print_sorted_dictionary(a_dictionary):
    """a function that prints a dictionary by ordered keys"""
    for keys, values in sorted(a_dictionary.items()):
        print("{}: {}".format(keys, values))


main()
