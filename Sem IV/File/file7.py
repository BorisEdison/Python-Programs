import os.path
def add_some_text():
    file1 = open("txt8.txt","a")
    l =  [ "More text added\n"]
    file1.writelines(l)
    file1.write("Here is some additional text \n")
    file1.close()
    file = open("txt8.txt","r+")
    print("Output of read function is ")
    print(file1.read())
    print()

add_some_text()