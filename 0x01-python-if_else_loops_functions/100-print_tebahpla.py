#!/usr/bin/python3
# a loop iterator i that that starts from the 1st ascii equivalent a - z
# an if statement that checks if i % 2 != 0
# if it is subtract -32 from i to get the uppercase letters
# print the alphabets

for i in range(122, 96, -1):
    if i % 2 != 0:
        i -= 32
    print("{}".format(chr(i)), end="")
