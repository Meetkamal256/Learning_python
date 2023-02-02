def common_elements(set_1, set_2):
    """a function that returns a set of common elements in two sets."""
    return set_1 & set_2


def main():
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))


main()
