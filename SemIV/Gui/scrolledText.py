import tkinter


import tkinter as tk
from tkinter import ttk 
from tkinter import scrolledtext

#from tkinter import scrolled text
#creating tkinter main window
win = tk.Tk()
win.title("ScrolledText Widget")

#Title label
ttk.Label(win,text="ScrolledText Widget Example",font=("Times New Roman",15),background="green",foregroun="white").grid(column=0,row=0)

#creating scrolled text   
#area widget 
text_area=scrolledtext.ScrolledText(win,wrap=tk.WORD,width=40,height=10,font=("Times New Roman",15))

text_area.grid(column=0,pady=10,padx=10)

#placing cursor in the text area
text_area.focus()
win.mainloop()