import os.path
# write data in a file.
file1 = open("txt5.txt","w")

L = ["this is SE COMPS \n","this is python lab\n","this is DBIT \n"]

# \n is placed to indicate EOL (end of lin)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file acess odes

file1 = open("txt5.txt","r+")


print("Output of Read function is: ")
print(file1.read())
print()

# seek(n) take the file handle to the nth
# bile from the begining 
# file1.seek(0)
 
print("Output of readline function is ")
print(file1.readline())
print()