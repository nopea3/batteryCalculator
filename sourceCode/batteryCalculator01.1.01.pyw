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


#under me is the volt/amph askers

def SvisualActivateQ30(devideVoltage, v, devideAmph, s):
    a = v/devideVoltage
    b = s/devideAmph
    w, wh, btPrice, btVoltage, btAmpH, cellCount, ampsBig, cycles = bt.visual('q30', a, b)
    messageValues = [ 'Voltage', btVoltage, '\n', 'Amps', ampsBig, '\n', 'Amphours', btAmpH, '\n', 'Cells', cellCount, '\n', 'w', w, '\n', wh, 'wh', '\n', 'cost', btPrice, '\n', 'Cells Used', 'q30', '\n', 'Battery cycles', cycles]
    tk.messagebox.showinfo(title= 'Your battery data', message = messageValues)


def SvisualActivateLgMj1(devideVoltage, v, devideAmph, s):
    a = v/devideVoltage
    b = s/devideAmph

    w, wh, btPrice, btVoltage, btAmpH, cellCount, ampsBig, cycles = bt.visual('Lg mj1', a, b)
    messageValues = [ 'Voltage', btVoltage, '\n' , 'Amps', ampsBig, '\n',  'Amphours', btAmpH, '\n', 'Cells', cellCount, '\n', 'w', w, '\n', wh, 'wh', '\n', 'cost', btPrice, '\n', 'Cells Used', 'Lg mj1', '\n', 'Battery cycles', cycles]
    tk.messagebox.showinfo(title= 'Your battery data', message = messageValues)

def SvisualActivateCustom(batteryVoltage, batteryAmphours):
    voltage, amphours, maxCharge, amps, price, cellCycles = bt.identifyCelltype('custom')
    cellsInSeries = batteryVoltage / voltage
    cellsInParallel = batteryAmphours / amphours
    wh = voltage * cellsInSeries * amphours * cellsInParallel
    voltageBig = voltage * cellsInSeries
    ampsBig = amps * cellsInParallel
    w = voltageBig * ampsBig
    btPrice = price * cellsInSeries * cellsInParallel
    btVoltage = voltage * cellsInSeries
    btAmpH = amphours * cellsInParallel
    cellCount = cellsInParallel * cellsInSeries

    canvasCustom = tk.Canvas(root, width= 200, height=200)

    messageValues = [ 'Voltage', btVoltage, '\n' , 'Amps', ampsBig, '\n', 'Amphours', btAmpH, '\n', 'Cells', cellCount, '\n', 'w', w, '\n', wh, 'wh', '\n', 'cost', btPrice, '\n', 'Cells Used', 'Custom', '\n', 'Battery cycles', cellCycles]
    tk.messagebox.showinfo(title= 'Your battery data', message = messageValues)



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


    s = tk.Button(root, text='Ok', command=root.quit)
    s.grid(row=3, column=1)
   
    root.mainloop()
    batteryVoltage = float(v1.get())
    batteryAmphours = float(a1.get())
    root.destroy()

    root = tk.Tk()
    entry1 = tk.Entry()
    root.title('What cells do you want to use')
    canvas6 = tk.Canvas(root, width = 400, height = 100)
    canvas6.grid()

    B = tk.Button(root, text='q30 kenno', command=lambda: SvisualActivateQ30(3.6, batteryVoltage, 3.0, batteryAmphours))
    C = tk.Button(root, text='Lg mj1 kenno', command=lambda: SvisualActivateLgMj1(3.63, batteryVoltage, 3.5, batteryAmphours))
    F = tk.Button(root, text='Custom kenno', command=lambda: [SvisualActivateCustom(batteryVoltage, batteryAmphours), root.destroy()])
    
    B.grid(row=3, column=1)
    C.grid(row=4, column=1)
    F.grid(row=5, column=1)
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
