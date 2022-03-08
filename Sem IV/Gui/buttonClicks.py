import tkinter 
from tkinter import *
window=tkinter.Tk()
window.title("Welcome to Event Handling")

def LC(event):
    Label(window,text="left click").pack()

def MC(event):
    Label(window,text="middle clicked!!!").pack()

def RC(event):
    Label(window,text="right clicked!!!").pack()

window.bind("<Button-1>",LC)
window.bind("<Button-2>",MC)
window.bind("<Button-3>",RC)

window.mainloop()