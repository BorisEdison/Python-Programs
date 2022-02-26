import os 
def create_another_file():
    if os.path.isfile('test.txt'):
        print('Trying to create a existing file')
    else:
        f = open('c:/test.txt',"w")
        f.write("This is how you create new text file")