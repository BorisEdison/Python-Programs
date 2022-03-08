from tkinter import *
from tkinter import messagebox

def push():
    # print("you selected ketchup")
    messagebox.showinfo("message","you selected ketchup")


def push1():
    # print("You selected Mayo")
    messagebox.showinfo("message","you selected Mayo")

import tkinter

top = Tk()
mb = Menubutton (top, text = "condiments",relief= RAISED)

mb.grid()

mb.menu = Menu(mb,tearoff = 0)
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton(label = "mayo",variable = mayoVar, command=push1)
mb.menu.add_checkbutton(label = "ketchup",variable = ketchVar, command=push)

mb.pack()
top.mainloop()