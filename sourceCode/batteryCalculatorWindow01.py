import tkinter as tk
import batteryCalculatorReWrite as bt



def visualActivateQ30():
    w, wh, btPrice, btVoltage, btAmpH, cellCount = bt.visual('q30', 20, 20)
    print(btVoltage,'Voltage')
    print(btAmpH,'Amphours')
    print(cellCount, 'cells')
    print(w,'w')
    print(wh,'wh')
    print(btPrice,'€')
    print('q30')

def visualActivateLgMj1():
    w, wh, btPrice, btVoltage, btAmpH, cellCount = bt.visual('Lg mj1', 20, 20)
    print(btVoltage,'Voltage')
    print(btAmpH,'Amphours')
    print(cellCount, 'cells')
    print(w,'w')
    print(wh,'wh')
    print(btPrice,'€')
    print('Lg mj1')

def visualActivateCustom():
    w, wh, btPrice, btVoltage, btAmpH, cellCount = bt.visual('Custom', 20, 20)
    print(btVoltage,'Voltage')
    print(btAmpH,'Amphours')
    print(cellCount, 'cells')
    print(w,'w')
    print(wh,'wh')
    print(btPrice,'€')

root = tk.Tk()
entry1 = tk.Entry()


canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.grid()


B = tk.Button(root, text='q30 kenno', command=visualActivateQ30())
C = tk.Button(root, text='Lg mj1', command=visualActivateLgMj1())


B.grid(row=1, column=1)
C.grid(row=2, column=1)

root.mainloop()