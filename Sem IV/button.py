from tkinter import *

def exit():
    # print("Button Pushed")
    exit()

def buttonPushed():
    print("Button pressed")
    var = StringVar()
    label = Label(root,textvariable=var,relief= RAISED)
    var.set("Hey? How are you doing?")
    label.pack()

root = Tk()
w=Label(root,text="Hello world")
w.pack()

myButton1 = Button(root,text="EXIT",command = exit)
myButton2 = Button(root,text="press",command = buttonPushed)

myButton1.pack()
myButton2.pack()
root.mainloop()