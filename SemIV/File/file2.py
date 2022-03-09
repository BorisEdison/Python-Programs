import os
fo = open("test3.txt","r")
str = fo.read(10)

print ("Read String is:",str)
position = fo.tell()
print ("Current file position: ",position)
position = fo.seek(0,0)
str = fo.read(10)
print("Again read String is: ", str)
fo.close()
