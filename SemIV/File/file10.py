import os.path
def split_fully(path):
    parent_path, name = os.path.split(path)
    if name =="":
        return(parent_path,)
    else: 
        return split_fully(parent_path)+(name,)
print(split_fully("C://user//Admin//AppData//Programs//Python"))
