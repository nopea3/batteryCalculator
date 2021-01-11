import tkinter as tk
import batteryCalculatorReWrite as bt



def visualActivateQ30(a,b):
    w, wh, btPrice, btVoltage, btAmpH, cellCount = bt.visual('q30', a, b)
    print(btVoltage,'Voltage')
    print(btAmpH,'Amphours')
    print(cellCount, 'cells')
    print(w,'w')
    print(wh,'wh')
    print(btPrice,'€')
    print('q30')

def visualActivateLgMj1(a,b):
    w, wh, btPrice, btVoltage, btAmpH, cellCount = bt.visual('Lg mj1', a,b)
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

entry1 = tk.Label(root, height=160, width=160, text='montako kennoa pistetään Sarjaan')
entry1 = tk.Entry (root)
canvas1.create_window(200, 160, window=entry1)
#a.grid(row=5, column= 5)
b = tk.Label(root, height=160, width=140, text='montako kennoa pistetään Rinnakkain')
b = tk.Entry (root)
canvas1.create_window(200, 140, window=b)



B = tk.Button(root, text='q30 kenno', command=visualActivateQ30(10,10))
C = tk.Button(root, text='Lg mj1', command=visualActivateLgMj1(10,10))
#B = tk.Button(root, text='Custom', command=visualActivateCustom)


B.grid(row=1, column=1)
C.grid(row=2, column=1)
#C.pack()
root.mainloop()