#!/usr/bin/python3
from sys import argv


def main():
    sum_result = 0
    for i in range(1, len(argv)):
        sum_result += int(argv[i])
    print(sum_result)


if __name__ == '__main__':
    main()
