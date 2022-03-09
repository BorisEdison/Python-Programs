import os
fo = open("test.txt","w+")
fo.write("Boris Edison\n14")
fo.close()
fo = open("test.txt","r")
print(fo.read())