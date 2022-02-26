import os
fo = open("test4.txt","r")
str = fo.read()
fo.close()
fo = open("test5.txt","w")
fo.write(str)
fo.close()