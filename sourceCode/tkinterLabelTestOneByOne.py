import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

#entry1 = tk.Entry (root)
#canvas1.create_window(200, 140, window=entry1)

print(canvas1)

#def getSquareRoot ():  
    #x1 = entry1.get()
    
    #label1 = tk.Label(root, text= float(10)**0.5)
    #canvas1.create_window(200, 230, window=label1)

#getSquareRoot()

root.mainloop()