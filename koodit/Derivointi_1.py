import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(-5,5,100)
y = np.power(x,2)

xa = 2
for i in range(10):
    learningRate = 1
    derivaatta = 2 * xa
    xa = xa - derivaatta * learningRate
    ya = np.power(xa,2)

    plt.figure(1)
    plt.subplot(5,2,i+1), plt.plot(x,y),plt.plot(xa,ya,'r*')
plt.show()