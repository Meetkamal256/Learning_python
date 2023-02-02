def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""
    a = {}
    for i in a_dictionary:
        a[i] = (a_dictionary[i] * 2)
    return a


def main():
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)


def print_sorted_dictionary(a_dictionary):
    """a function that prints a dictionary by ordered keys"""
    for keys, values in sorted(a_dictionary.items()):
        print("{}: {}".format(keys, values))


main()
