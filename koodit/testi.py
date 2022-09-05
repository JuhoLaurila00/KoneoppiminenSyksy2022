import numpy as np
import matplotlib.pyplot as plt

class signalAnalyser:
    def __init__(self,Fs,t):
        print('Constructor of signalAnalyser')
        self.Fs = Fs
        self.Ts = 1/Fs
        self.t = t
        self.xakseli = np.arange(0,t,self.Ts)       # Tehdään x-akseli
        self.pituus = int(self.xakseli.size)        # Määritetään x-akselin pituus
        self.yakseli = np.zeros((1,self.pituus))    # Tehdään y-akseli
        
    

    def create(self,f):
        pii = np.pi
        t = self.xakseli
        
        self.yakseli = np.cos( 2 * pii * f * t)     # Määritetään signaali
        self.Syakseli = np.sin( 2 * pii * f * t)    
        self.Tyakseli = np.tan( 2 * pii * f * t)
        
        


    def plot(self,start,stop):
        x = self.xakseli
        y1 = self.yakseli
        y2 = self.Syakseli
        y3 = self.Tyakseli
        fig, ax = plt.subplots(3)
        ax[0].plot(x[start:stop],y1[start:stop],'-*')
        ax[1].plot(x[start:stop],y2[start:stop],'-*')
        ax[2].plot(x[start:stop],y3[start:stop],'-*')
        plt.figure(1)
        
        plt.show()   

if __name__ == '__main__':
    obj = signalAnalyser(1000,2)  # luodaan objekti, jonka konstruktorille Fs = 100 Hz ja t = 2s
    obj.create(10)                # käytetään objektin create funktiota, missä f = 2 Hz
    obj.plot(0,2000)               # käytetään objektin plot funktiota, plotataan väli 0 - 50 näytettä.
