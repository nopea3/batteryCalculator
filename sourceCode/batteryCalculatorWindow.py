import tkinter as tk
import batteryCalculatorReWrite

root = tk.Tk()
entry1 = tk.Entry()

canvas1 = tk.Canvas(root, width = 400, height= 400)
canvas1.pack()

centry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

root.mainloop()