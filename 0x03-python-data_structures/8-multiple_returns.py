#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "":
        first_char = sentence[0]
    else:
        if sentence == "":
            first_char = None
    return len(sentence), first_char


def main():
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))


main()
