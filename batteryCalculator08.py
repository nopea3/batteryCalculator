import os
import sys

def batteryNameDetection(Bcell):
        
    if Bcell == 'Lg mj1':
        voltage =  3.63
        amphours =  3.5
        maxCharge =  3.5
        maxDischargeCurrent = 10
        price = 3.45
        return (voltage, amphours, maxCharge, maxDischargeCurrent, price)

    if Bcell == 'q30' or '30q':
        voltage =  3.6
        amphours = 3.0
        maxCharge = 4.2
        maxDischargeCurrent = 20.0
        price = 3.75
        return (voltage, amphours, maxCharge, maxDischargeCurrent, price)

    if Bcell == 'custom':
        voltage = float(input('Kennon voltit '))
        amphours = int(input('Kennon ampperitunnit '))
        maxCharge = int(input('maksimi voltit mitä kennoon voi ladata '))
        maxDischargeCurrent = int(input('kuinka paljon kennosta voi ottaa amppeereita '))
        price = int(input('Kennon hinta'))
        return (voltage, amphours, maxCharge, maxDischargeCurrent, price)

    else:
        quit()
    

def cellCount():
    voltage, amphours, maxCapasity, amps, p = batteryNameDetection(Bcell)

    serialCellCount = int(input('Kuinka monta kennoa haluat kytkeä SARJAAN '))
    parallelCellCount = int(input('Kuinka monta kennoa haluat kytkeä RINNAN '))

    wholeBatteryVoltage = voltage * serialCellCount
    wholeBatteryAmphours = amphours * parallelCellCount
    #amps = 

    return wholeBatteryVoltage, wholeBatteryAmphours, serialCellCount, parallelCellCount, amps

def batteryStats():
    batteryVoltage, batteryAmphours, serialCells, parallelCells, amps = cellCount()
    smallVolts, smallAmphours, maxCapasity, a, p = batteryNameDetection(Bcell)
    price = p

    cells = serialCells * parallelCells

    batteryPrice = cells * price
    maxPower = batteryVoltage * a * serialCells
    capasity = batteryVoltage * batteryAmphours


    return batteryVoltage, batteryAmphours, serialCells, parallelCells, maxPower, capasity, batteryPrice



if __name__ == "__main__":
    
    Bcell = input('minkä kennon haluat ')

    #calculateBatteryCapasity(Bcell)

    batteryVoltage, batteryAmphours, serialCells, parallelCells, maxPower, capasity, price = batteryStats()

    print('voltage', batteryVoltage)
    print('Amphours', batteryAmphours)
    print(serialCells,'s')
    print(parallelCells,'p')
    w = round(maxPower,3)
    print(w, 'w')
    kw = round(maxPower/1000,3)
    print(kw,'kw')
    print(capasity,'wh')
    kwh = round(capasity/1000, 3)
    print(kwh,'kwh')
    print(price, '€')

    k = input('paina enter sulkeaksesi')
    

    
    

