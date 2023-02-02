import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("some random text\nMore random text\nAnd more")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())

print(myFile.closed)
print(myFile.name)
print(myFile.mode)

os.rename("mydata.txt", "mydata2.txt")
os.remove("mydata2.txt")
# os.mkdir("mydir")
os.chdir("mydir")
print("current Directory:", os.getcwd())
os.chdir("..")
print("current Directory:", os.getcwd())
os.rmdir("mydir")




