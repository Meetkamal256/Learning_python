def update_dictionary(a_dictionary, key, value):
    """replaces or adds key/value in a dictionary """
    for i in a_dictionary:
        if i is key:
            a_dictionary[i] = value
    else:
        a_dictionary[key] = value
    return a_dictionary


def main():
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)


def print_sorted_dictionary(a_dictionary):
    """a function that prints a dictionary by ordered keys"""
    for keys, values in sorted(a_dictionary.items()):
        print("{}: {}".format(keys, values))


main()
