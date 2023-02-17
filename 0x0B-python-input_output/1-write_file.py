#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8) 
and returns the number of characters written:
"""
def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
    
    
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
