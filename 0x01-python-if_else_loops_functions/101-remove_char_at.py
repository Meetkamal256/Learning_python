#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    for char in str:
        if n > len(str):
            return str
        if char != str[n]:
            # print("{}".format(char), end="")
            new_string += char
    return new_string


def main():
    print(remove_char_at("Best School", 3))
    print(remove_char_at("Chicago", 2))
    print(remove_char_at("C is fun!", 0))
    print(remove_char_at("School", 10))
    print(remove_char_at("Python", -2))


main()
