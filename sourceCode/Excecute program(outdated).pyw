import tkinter as tk
from tkinter import messagebox
import batteryCalculatorReWrite01 as bt


def visualActivateQ30():

    a = float(e1.get())
    b = float(e2.get())

    w, wh, btPrice, btVoltage, btAmpH, cellCount, ampsBig = bt.visual('q30', a, b)
    messageValues = [ 'Voltage', btVoltage, '\n', 'Amps', ampsBig, '\n', 'Amphours', btAmpH, '\n', 'Cells', cellCount, '\n', 'w', w, '\n', wh, 'wh', '\n', 'cost', btPrice, '\n', 'Cells Used', 'q30']
    tk.messagebox.showinfo(title= 'Your battery data', message = messageValues)


def visualActivateLgMj1():
    a = float(e1.get())
    b = float(e2.get())

    w, wh, btPrice, btVoltage, btAmpH, cellCount, ampsBig = bt.visual('Lg mj1', a, b)
    messageValues = [ 'Voltage', btVoltage, '\n' , 'Amps', ampsBig, '\n',  'Amphours', btAmpH, '\n', 'Cells', cellCount, '\n', 'w', w, '\n', wh, 'wh', '\n', 'cost', btPrice, '\n', 'Cells Used', 'Lg mj1']
    tk.messagebox.showinfo(title= 'Your battery data', message = messageValues)

def visualActivateCustom():
    canvasCustom = tk.Canvas(root, width= 200, height=200)
    a = float(e1.get())
    b = float(e2.get())

    w, wh, btPrice, btVoltage, btAmpH, cellCount, ampsBig = bt.visual('custom', a, b)

    messageValues = [ 'Voltage', btVoltage, '\n' , 'Amps', ampsBig, '\n', 'Amphours', btAmpH, '\n', 'Cells', cellCount, '\n', 'w', w, '\n', wh, 'wh', '\n', 'cost', btPrice, '\n', 'Cells Used', 'Custom']
    tk.messagebox.showinfo(title= 'Your battery data', message = messageValues)

root = tk.Tk()
entry1 = tk.Entry()
root.title('Battery Calculator')


canvas1 = tk.Canvas(root, width = 200, height = 200)

canvas1.grid()

tk.Label(root, text="Montako kennoa sarjaan").grid(row=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)

tk.Label(root, text="Montako kennoa rinnan").grid(row=1)
e2 = tk.Entry(root)
e2.grid(row=1, column=1)


B = tk.Button(root, text='q30 kenno', command=visualActivateQ30)
C = tk.Button(root, text='Lg mj1 kenno', command=visualActivateLgMj1)
F = tk.Button(root, text='Custom kenno', command= visualActivateCustom)


B.grid(row=3, column=1)
C.grid(row=4, column=1)
F.grid(row=5, column=1)

canvas1.place(x=800,y=600)

root.mainloop()
