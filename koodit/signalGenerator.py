from multiprocessing.resource_sharer import stop
from tracemalloc import start
from W1_T3 import signalAnalyser  as analyzer
import numpy as np
import matplotlib.pyplot as plt

def t3():
    aika = int(input("Anna aika 1-10: "))
    print(aika)
    taajuus = int(input("Anna taajuus 0-500: "))
    print(taajuus)
    maara = int(input("Pisteiden maara: "))

    obj = analyzer(100,aika)
    obj.create(taajuus)
    obj.plot(0,maara)

t3()