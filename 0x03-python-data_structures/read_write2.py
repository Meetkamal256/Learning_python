import os

with open("mydata.txt2", mode="w", encoding= "utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")

with open("mydata.txt2", encoding="utf-8") as myFile:
    line_num = 1  # tracks the line number
    while True:  # loops till the data is all read
        line = myFile.readline()  # reads one line at a time up to the new line

        if not line:  # if line doesn't have any data then break out of the loop
            break
            print("line", line_num)

        # split()
        word_list = line.split()
        # len() find number of words available inside each len


        # loop and count the characters in the list

        # divide the character count / len word list

        line_num += 1
