import os.path

firstfile = open("text5.txt","r+")
secondfile = open("text7.txt","w+")
for line in firstfile:
    secondfile.write(line)