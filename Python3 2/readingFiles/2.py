import os
coun_file = open('C:/Users/acer/Desktop/Boris/python/Python-Programs/Python3 2/readingFiles/countries.txt','r')

print(coun_file.readline())
print(coun_file.readline())
print(coun_file.readlines())

for lines1 in coun_file.readlines():
    print(lines1)
coun_file.close()
