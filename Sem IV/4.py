from tkinter import *;

root = Tk()
root.title("4.py")
var = StringVar()

label = Label(root,textvariable=var,relief= RAISED)

var.set("Hey? How are you doing?")
root.geometry('350x200')
label.grid(column=3,row=23)
label.pack()
root.mainloop()