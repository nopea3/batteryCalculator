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

canvas1 = tk.Canvas(root, width = 400, height= 400)
canvas1.grid()

centry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

B = tk.Button(root, text='q30 kenno', command=visualActivateQ30)
C = tk.Button(root, text='Lg mj1', command=visualActivateLgMj1)
#B = tk.Button(root, text='Custom', command=visualActivateCustom)


B.grid(row=1, column=1)
C.grid(row=2, column=1)
#C.pack()
root.mainloop()