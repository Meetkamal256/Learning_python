#!/usr/bin/python3
"""
appends a string at the end of a text file (UTF8) and 
returns the number of characters added
"""
def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
    

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
