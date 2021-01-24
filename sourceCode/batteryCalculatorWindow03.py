import tkinter as tk
from tkinter import messagebox
import batteryCalculatorReWrite01 as bt


def visualActivateQ30():

    a = float(e1.get())
    b = float(e2.get())

    w, wh, btPrice, btVoltage, btAmpH, cellCount, ampsBig, cycles = bt.visual('q30', a, b)
    messageValues = [ 'Voltage', btVoltage, '\n', 'Amps', ampsBig, '\n', 'Amphours', btAmpH, '\n', 'Cells', cellCount, '\n', 'w', w, '\n', wh, 'wh', '\n', 'cost', btPrice, '\n', 'Cells Used', 'q30', '\n', 'Battery cycles', cycles]
    tk.messagebox.showinfo(title= 'Your battery data', message = messageValues)


def visualActivateLgMj1():
    a = float(e1.get())
    b = float(e2.get())

    w, wh, btPrice, btVoltage, btAmpH, cellCount, ampsBig, cycles = bt.visual('Lg mj1', a, b)
    messageValues = [ 'Voltage', btVoltage, '\n' , 'Amps', ampsBig, '\n',  'Amphours', btAmpH, '\n', 'Cells', cellCount, '\n', 'w', w, '\n', wh, 'wh', '\n', 'cost', btPrice, '\n', 'Cells Used', 'Lg mj1', '\n', 'Battery cycles', cycles]
    tk.messagebox.showinfo(title= 'Your battery data', message = messageValues)

def visualActivateCustom():
    canvasCustom = tk.Canvas(root, width= 200, height=200)
    a = float(e1.get())
    b = float(e2.get())

    w, wh, btPrice, btVoltage, btAmpH, cellCount, ampsBig, cycles = bt.visual('custom', a, b)

    messageValues = [ 'Voltage', btVoltage, '\n' , 'Amps', ampsBig, '\n', 'Amphours', btAmpH, '\n', 'Cells', cellCount, '\n', 'w', w, '\n', wh, 'wh', '\n', 'cost', btPrice, '\n', 'Cells Used', 'Custom', '\n', 'Battery cycles', cycles]
    tk.messagebox.showinfo(title= 'Your battery data', message = messageValues)


def collectVoltValues():
    batteryVoltage = v1.float(get())
    batteryAmphours = a1.folat(get())  
    return batteryVoltage, batteryAmphours

def askForValues():
    root = tk.Tk()
    entry1 = tk.Entry()
    root.title('Input Voltages and amphours')
    canvas5 = tk.Canvas(root, width = 400, height = 100)
    canvas5.grid()
    tk.Label(root, text="Voltage").grid(row=0)
    v1 = tk.Entry(root)
    v1.grid(row=0, column=1)
    
    tk.Label(root, text="Amphours").grid(row=1)
    a1 = tk.Entry(root)
    a1.grid(row=1, column=1)


    s = tk.Button(root, text='Ok', command=root.quit())
    s.grid(row=3, column=1)
   
    root.mainloop()
    batteryVoltage, batteryAmphours = collectVoltValues()
    return batteryVoltage, batteryAmphours


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
g = tk.Button(root, text='Insert cells by voltage and amps/amphours', command=askForValues)



B.grid(row=3, column=1)
C.grid(row=4, column=1)
F.grid(row=5, column=1)
g.grid(row=6, column=1)

canvas1.place(x=800,y=600)

root.mainloop()
