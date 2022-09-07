from W1_T3 import signalAnalyser  as analyzer
import numpy as np
import matplotlib.pyplot as plt

def t3():
    aika = int(input("Anna aika 1-10: "))
    print(aika)
    taajuus = int(input("Anna taajuus 0-500: "))
    print(taajuus)
    rate = int(input("Anna näytteenottotaajuus: "))
    print(rate)
    maara = rate * aika #kerrotaan näytteenottotaajuus ajalla, jotta näytteitä on haluttu maara per sekunti, ajasta riippumatta

    obj = analyzer(rate,aika)
    obj.create(taajuus)
    obj.plot(0,maara)

t3()