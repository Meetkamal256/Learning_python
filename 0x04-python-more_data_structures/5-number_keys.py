def number_keys(a_dictionary):
    """a function that returns the number of keys in a dictionary."""
    return len(a_dictionary)


def main():
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))


main()