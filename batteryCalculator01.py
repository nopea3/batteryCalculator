
class inputs():
    voltage = 0
    peakAmps = 0
    amphours = 0
    maxCharge = 0
    maxDischargeCurrent = 0

    def batteryProperty(self, batteryCell):
        pass

    def batteryNameDetection(self, Bcell, voltage, amphours, maxCharge, maxDischargeCurrent):
        if Bcell == 'Lg mj1':
            voltage = 3.63
            amphours = 3.5
            maxCharge = 4.2
            maxDischargeCurrent = 10

            return voltage, amphours, maxCharge, maxDischargeCurrent
            
        


if __name__ == "__main__":

    Bcell = ''

    inputs().batteryProperty(Bcell)
    
    
    Bcell = input('minkä akun haluat')
    pass

