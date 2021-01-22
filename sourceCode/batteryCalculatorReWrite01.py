import time
import tkinter as tk
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import html.parser


import urllib.request

#with urllib.request.urlopen("https://www.nkon.nl/products/4x-varta-aaa-industrial.html") as url:
#    s = url.read()
#    soup = BeautifulSoup(html.parser.content, 'html.parser')
#    soup.find_all('p', class_='price')
#    print(s)


def askForCellType():
    name = input('Minkä kennon haluat ')
    oikeatNimet = ['q30', 'Lg mj1', '30q', 'custom']

    testi = True
    for i in oikeatNimet:
        if i == name:
            testi = False
    
    if testi:
        quit()
    
    series = int(input('Montako kennoa haluat SARJAAN '))
    parallel = int(input('Montako kennoa haluat RINNAN '))
    return name, series, parallel

def identifyCelltype(Bcell):
    if Bcell == 'q30':
        voltage =  3.6
        amphours = 3.0
        maxCharge = 4.2
        amps = 20.0
        price = 3.75
        return voltage, amphours, maxCharge, amps, price

    if Bcell == 'Lg mj1':
        voltage =  3.63
        amphours =  3.5
        maxCharge =  3.5
        amps = 10
        price = 3.45
        return voltage, amphours, maxCharge, amps, price

    if Bcell == 'custom':
        root = tk.Tk()
        entry1 = tk.Entry()
        root.title('Custom cell data')
        canvas1 = tk.Canvas(root, width = 200, height = 150)
        canvas1.grid()
        tk.Label(root, text="Voltage").grid(row=0)
        e1 = tk.Entry(root)
        e1.grid(row=0, column=1)

        root.mainloop()
        voltage = float(input('voltage '))
        amphours = float(input('amphours '))
        maxCharge = float(input('maxCharge (voltage) '))
        amps = float(input('amps '))
        price = float(input('price '))
        
        #print(voltage, amphours, maxCharge, amps, price)

        return voltage, amphours, maxCharge, amps, price

    

def calculatePrices(voltage, amphours, maxCharge, amps, price, cellsInSeries, cellsInParallel):
    wh = voltage * cellsInSeries * amphours * cellsInParallel
    voltageBig = voltage * cellsInSeries
    ampsBig = amps * cellsInParallel
    w = voltageBig * ampsBig
    btPrice = price * cellsInSeries * cellsInParallel
    btVoltage = voltage * cellsInSeries
    btAmpH = amphours * cellsInParallel
    cellCount = cellsInParallel * cellsInSeries
    return w, wh, btPrice, btVoltage, btAmpH, cellCount, ampsBig

def visual(x, cellsInSeries, cellsInParallel):
    Bcell = x
    voltage, amphours, maxCharge, amps, price = identifyCelltype(Bcell)
    w, wh, btPrice, btVoltage, btAmpH, cellCount, ampsBig = calculatePrices(voltage, amphours, maxCharge, amps, price, cellsInSeries, cellsInParallel)
    return w, wh, btPrice, btVoltage, btAmpH, cellCount, ampsBig

#Bcell, cellsInSeries, cellsInParallel = askForCellType()
#voltage, amphours, maxCharge, amps, price = identifyCelltype(Bcell)
#w, wh, btPrice, btVoltage, btAmpH, cellCount = calculatePrices(voltage, amphours, maxCharge, amps, price, cellsInSeries, cellsInParallel)

#time.sleep(10)