import tkinter
from tkinter.ttk import *
window=tkinter.Tk()

combo=Combobox(window)
combo["values"]=[1,2,3,4,5,"Don't know"]

combo.current(3)
combo.grid(column=0,row=0)
window.mainloop()