
def executeProgram():

    Bcell = input('minkä akun haluat ')

    def batteryNameDetection(Bcell):
        
        voltage = 0.0
        amphours = 0.0
        maxCharge = 0.0
        maxDischargeCurrent = 0.0
        
        
        if Bcell == 'Lg mj1':
            voltage =  float(3.63)
            amphours =  float(3.5)
            maxCharge =  float(4.2)
            maxDischargeCurrent = float(10)
            return (voltage, amphours, maxCharge, maxDischargeCurrent)
        if Bcell == 'q30':
            voltage =  float(3.6)
            amphours = float(3)
            maxCharge = float(4.2)
            maxDischargeCurrent = float(20)
            return (voltage, amphours, maxCharge, maxDischargeCurrent)
        else:
            quit()
    

    def calculateBatteryCapasity(Bcell):
        batteryNameDetection(Bcell)

        peakPower = 0.0
        cellSize = 0.0

        peakPower = voltage * maxDischargeCurrent
        print('peakpower in watts ', peakPower)

        cellSize = voltage * amphours
        print('cellSize', cellSize)

        return (peakPower, cellSize)

    calculateBatteryCapasity(Bcell)

    print('voltage line 45',voltage)
    print('amps line 46', maxDischargeCurrent)
      

if __name__ == "__main__":
    
    
    executeProgram()
    
    pass

