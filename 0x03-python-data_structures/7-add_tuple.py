#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds two tuples together"""
    i = 0
    x = list(tuple_a)
    y = list(tuple_b)
    add_tuple = []

    while i < 2:
        if len(x) < 2:
            x.append(0)
        if len(y) < 2:
            y.append(0)
        add_tuple.append(x[i] + y[i])
        i += 1
    return tuple(add_tuple)


def main():
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))


main()
