
voltage = 0
amphours = 0
maxCharge = 0
maxDischargeCurrent = 0
peakPower = 0
cellSize = 0

def executeProgram():

    def batteryNameDetection(Bcell, voltage, amphours, maxCharge, maxDischargeCurrent):
        if Bcell == 'Lg mj1':
            voltage = 3.63
            amphours = 3.5
            maxCharge = 4.2
            maxDischargeCurrent = 10
            return (voltage, amphours, maxCharge, maxDischargeCurrent)

        if Bcell == 'q30':
            voltage = 3.6
            amphours = 3
            maxCharge = 4.2
            maxDischargeCurrent = 20
            return (voltage, amphours, maxCharge, maxDischargeCurrent)



    def calculateBatteryCapasity(Bcell, voltage, amphours, maxCharge, maxDischargeCurrent):
        batteryNameDetection(Bcell, voltage, amphours, maxCharge, maxDischargeCurrent)
        
        peakPower = voltage * maxDischargeCurrent
        print('peakpower in watts ', peakPower)

        cellSize = voltage * amphours
        print('cellSize', cellSize)

        return (peakPower, cellSize)
                
        


if __name__ == "__main__":

    Bcell = ''

    Bcell = input('minkä akun haluat')

    executeProgram()
    
    print('peakpower in watts ', peakPower)
    print('cellSize', cellSize)
    pass

