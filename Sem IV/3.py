from tkinter import *;

root = Tk()
root.title("3.py")
var = StringVar()

label = Message(root,textvariable=var,relief= RAISED,font = ("Arial bold",42))

var.set("Hey? How are you doing?")
label.pack()
root.mainloop()