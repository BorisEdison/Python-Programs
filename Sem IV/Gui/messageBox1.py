from ctypes.wintypes import SIZE
from tkinter import *
import tkinter


root = tkinter.Tk()
boolVar1 = BooleanVar()
boolVar2 = BooleanVar()

boolVar1.set(False)
boolVar2.set(False)

C1 = Checkbutton(root,text = "music",variable = boolVar1,onvalue = 1,offvalue = 0,height = 5,width = 20,font = ("Arial bold",42))

C2 = Checkbutton(root,text = "Video",variable = boolVar2,onvalue = 1,offvalue = 0,height = 5,width = 20)

C1.grid(row = 0, column = 0)
C2.grid(row = 0,column = 1)
root.mainloop()
