def uniq_add(my_list=[]):
    """a function that adds all unique integers in a list (only once for each integer)."""
    sum = 0
    for element in set(my_list):
        sum += element
    return sum


def main():
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))


main()
