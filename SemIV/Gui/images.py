import tkinter
from tkinter import PhotoImage

window = tkinter.Tk()

window.title("DBIT")


icon = tkinter.PhotoImage(file ="SemIV\Gui\DBIT.png")
label = tkinter.Label(window,image= icon)

label.pack()

window.mainloop()