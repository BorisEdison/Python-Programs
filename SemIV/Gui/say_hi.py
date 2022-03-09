import tkinter 
from tkinter import *
window=tkinter.Tk()
window.title("Welcome to Event Handling")

def say_hi(event):
    l=Label(window,text="one clicked!!!").pack()

btn1=tkinter.Button(window,text="ONE")
btn1.bind("<Button-3>",say_hi)
btn1.pack()

window.mainloop()