from tkinter import * 
import tkinter as tk 
root = Tk()
tk.Label(root, text="ok").grid(row=3)
e4 = tk.Entry(root)
e4.grid(row=3, column=1)
def woops():
    b = e4.get()
    a = 10
    return a, b
root.mainloop()

a, b = woops()
print(a, b)
