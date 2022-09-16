from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

Fs = 1000               #Sample Rate
Ts = 1/Fs               #Samples per second
t = np.arange(0,1,Ts)   #z-Akseli
f = 4                   #Taajuus
j = complex(0,1)        #?
s = np.exp(j*2*np.pi*f*t)   #Luodaan Signaali
z = t
x = np.real(s)              
y = np.imag(s)
ax.plot3D(x,y,z, 'red')     #Plotataan 3D spiraali
fig.suptitle('3D Balls In Vice') #Accurate

plt.show()