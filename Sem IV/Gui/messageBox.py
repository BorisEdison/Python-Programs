import tkinter
from tkinter import messagebox

top = tkinter.Tk()

top.geometry("100x100")

def helloCallBack():
    messagebox.showinfo("Hello Python","Hello World")
    exit()

B = tkinter.Button(top, text = "Hello", command = helloCallBack)

B.pack()
top.mainloop()