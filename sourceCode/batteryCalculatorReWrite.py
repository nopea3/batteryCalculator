import time
import requests

#response = requests.get('https://www.nkon.nl/lg-inr18650-mj1.html')
#print(response.json)

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
        voltage = float(input('voltage '))
        amphours = float(input('amphours '))
        maxCharge = float(input('maxCharge (voltage) '))
        amps = float(input('amps '))
        price = float(input('price '))
        
        #print(voltage, amphours, maxCharge, amps, price)

        return voltage, amphours, maxCharge, amps, price

    

def calculatePrices(voltage, amphours, maxCharge, amps, price, cellsInSeries, cellsInParallel):
    wh = voltage * cellsInSeries * amphours * cellsInParallel
    w = voltage * cellsInSeries * amps
    btPrice = price * cellsInSeries * cellsInParallel
    btVoltage = voltage * cellsInSeries
    btAmpH = amphours * cellsInParallel
    cellCount = cellsInParallel * cellsInSeries
    return w, wh, btPrice, btVoltage, btAmpH, cellCount

def visual(x, cellsInSeries, cellsInParallel):
    Bcell = x
    voltage, amphours, maxCharge, amps, price = identifyCelltype(Bcell)
    w, wh, btPrice, btVoltage, btAmpH, cellCount = calculatePrices(voltage, amphours, maxCharge, amps, price, cellsInSeries, cellsInParallel)
    return w, wh, btPrice, btVoltage, btAmpH, cellCount

#Bcell, cellsInSeries, cellsInParallel = askForCellType()
#voltage, amphours, maxCharge, amps, price = identifyCelltype(Bcell)
#w, wh, btPrice, btVoltage, btAmpH, cellCount = calculatePrices(voltage, amphours, maxCharge, amps, price, cellsInSeries, cellsInParallel)


#time.sleep(10)