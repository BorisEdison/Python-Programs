import os
file1 = open("test1.txt","w")
L = ["This is delhi\n","This is paris\n","this is London \n"]


file1.write("Hello \n")
file1.writelines(L)
file1.close()

file1 = open("test1.txt","r+")

print("OUtput of Read function is ")
print(file1.read())
print()

file1.seek(0)

print("Output of readline function is ")
print(file1.readline())
print()

file1.seek(0)