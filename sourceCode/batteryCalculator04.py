
voltage = 0
amphours = 0
maxCharge = 0
maxDischargeCurrent = 0
peakPower = 0
cellSize = 0
#Bcell = 'q30'

def executeProgram(Bcell,voltage, amphours, maxCharge, maxDischargeCurrent, peakPower, cellSize):

    def askBattery():
        Bcell = input('minkä akun haluat')
        print(Bcell)
        return (Bcell)

    def batteryNameDetection(Bcell, voltage, amphours, maxCharge, maxDischargeCurrent):
        if Bcell == 'Lg mj1':
            voltage =  float(3.63)
            amphours =  float(3.5)
            maxCharge =  float(4.2)
            maxDischargeCurrent = float(10)
            return (voltage, amphours, maxCharge, maxDischargeCurrent)

        if Bcell == 'q30':

            #voltage = 0
            #amphours = 0
            #maxCharge = 0
            #maxDischargeCurrent = 0
            
            voltage =  float(3.6)
            amphours = float(3)
            maxCharge = float(4.2)
            maxDischargeCurrent = float(20)

            return (voltage, amphours, maxCharge, maxDischargeCurrent)

        else:
            quit()



    def calculateBatteryCapasity(Bcell, voltage, amphours, maxCharge, maxDischargeCurrent, peakPower, cellSize):
        batteryNameDetection(Bcell, voltage, amphours, maxCharge, maxDischargeCurrent)

        peakPower = voltage * maxDischargeCurrent
        print('peakpower in watts ', peakPower)

        cellSize = voltage * amphours
        print('cellSize', cellSize)

        return (peakPower, cellSize)

    askBattery()
    calculateBatteryCapasity(Bcell, voltage, amphours, maxCharge, maxDischargeCurrent, peakPower, cellSize)

                
        


if __name__ == "__main__":

    Bcell = 'q30'
    executeProgram(Bcell, voltage, amphours, maxCharge, maxDischargeCurrent, peakPower, cellSize)
    
    pass

