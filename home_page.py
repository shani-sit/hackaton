# Import Module
from tkinter import *
from tkinter import ttk
import tkinter as tk


# create root window
root = Tk()
root.title("AddMajor") 
T = Text(root, height = 5, width = 52)

root.geometry('1000x1000')
l = Label(root, text = "AddMajor")
l.config(font =("Helvetica", 70))
l.pack()
nb = ttk.Notebook(root)

# Frame 1 and 2 and 3
frame1 = ttk.Frame(nb)
frame2 = ttk.Frame(nb)
frame3 = ttk.Frame(nb)

label1 = ttk.Label(frame1, text = "This is Window One")
label1.pack(pady = 1000, padx = 1000)
label2 = ttk.Label(frame2, text = "This is Window Two")
label2.pack(pady = 50, padx = 20)
label3 = ttk.Label(frame3, text = "This is Window Three")
label3.pack(pady = 50, padx = 20)

frame1.pack(fill= tk.BOTH, expand=True)
frame2.pack(fill= tk.BOTH, expand=True)
frame3.pack(fill= tk.BOTH, expand=True)

nb.add(frame1, text = "home Page" )



nb.add(frame2, text = "user")
nb.add(frame3, text = "Window 3")
nb.pack(padx = 5, pady = 5, expand = True)
# all widgets will be here
# Execute Tkinter
root.mainloop()