

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
        amphours = float(3)
        maxCharge = float(4.2)
        maxDischargeCurrent = float(20)
        price = 3.75
        return (voltage, amphours, maxCharge, maxDischargeCurrent, price)

    if Bcell == 'custom':
        voltage = int(input('Kennon voltit '))
        amphours = int(input('Kennon ampperitunnit '))
        maxCharge = int(input('maksimi voltit mitä kennoon voi ladata '))
        maxDischargeCurrent = int(input('kuinka paljon kennosta voi ottaa amppeereita '))
        price = int(input('Kennon hinta'))
        return (voltage, amphours, maxCharge, maxDischargeCurrent, price)

    else:
        quit()
    

def calculateBatteryCapasity(Bcell):
    a, b, c, d, p = batteryNameDetection(Bcell)

    peakPower = 0.0
    cellSize = 0.0
       
    cellSize = a * b
         
    print('cellSize', cellSize, 'wh')

    peakPower = a * d
    print('peakPower', peakPower, 'w')
    return (peakPower, cellSize, p)

def cellCount():
    voltage, amphours, maxCapasity, amps, p = batteryNameDetection(Bcell)
    serialCellCount = int(input('Kuinka monta kennoa haluat kytkeä SARJAAN '))
    parallelCellCount = int(input('Kuinka monta kennoa haluat kytkeä RINNAN '))

    wholeBatteryVoltage = voltage * serialCellCount
    wholeBatteryAmphours = amphours * parallelCellCount

    return wholeBatteryVoltage, wholeBatteryAmphours, serialCellCount, parallelCellCount

def batteryStats():
    batteryVoltage, batteryAmphours, serialCells, parallelCells = cellCount()
    smallVolts, smallAmphours, maxCapasity, amps, p = batteryNameDetection(Bcell)
    a, b, price = calculateBatteryCapasity(Bcell)

    maxPower = batteryVoltage * amps
    capasity = batteryVoltage * batteryAmphours

    cells = serialCells * parallelCells
    batteryPrice = cells * price
    
    return batteryVoltage, batteryAmphours, serialCells, parallelCells, maxPower, capasity, batteryPrice



if __name__ == "__main__":
    
    Bcell = input('minkä kennon haluat ')

    calculateBatteryCapasity(Bcell)

    batteryVoltage, batteryAmphours, serialCells, parallelCells, maxPower, capasity, price = batteryStats()

    print('voltage', batteryVoltage)
    print('Amphours', batteryAmphours)
    print(serialCells,'s')
    print(parallelCells,'p')
    print(maxPower, 'w')
    print(maxPower/1000,'kw')
    print(capasity,'wh')
    print(capasity/1000,'kwh')
    print(price, '€')
    

    
    

