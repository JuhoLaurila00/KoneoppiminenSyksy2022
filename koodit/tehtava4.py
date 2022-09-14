import numpy as np
import matplotlib.pyplot as plt
'''
Let's look in to matplotlib library properties and train ourselves
with Numpy array manipulations. Your tasks are the following:
1) Make 256*256 pixel picture (instructions given below). Current
   example plots RGB picture where Red component is all ones and G,B components are zero
   thus picture is all red. Your task is to modify picture in such a way that pixels
   at range 0-127 (rows), 0-127 (columns) show red picture area
   at range 0-127 (rows), 128-256 (columns) show green picture area
   at range 128-256 (row), 0-127 (columns) show blue picture area
   at range 128-256 (row), 128-256 (columns) show gray picture area 

'''
size = 256
kuva = np.zeros((size,size,3))
kuva[0:128,0:128,0]= np.ones((128,128))
kuva[0:128,128:256,1]= np.ones((128,128))
kuva[128:256,0:128,2]= np.ones((128,128))
kuva[128:256,128:256,0]= np.ones((128,128))*0.5
kuva[128:256,128:256,1]= np.ones((128,128))*0.5
kuva[128:256,128:256,2]= np.ones((128,128))*0.5
plt.imshow(kuva)
#plt.show()

'''
Let's look at matplotlib library basic usage tutorials. There is an example
how to create 3 figures as shown below

fig1 = plt.figure()  # an empty figure with no Axes
fig2, ax = plt.subplots()  # a figure with a single Axes
fig3, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

Your tasks are the following:
1) create 4 NumPy arrays containing 1 second sine signals with 1, 2, 3, 4 Hz
    HINT:
    create first time t = np.arange(0,1,0.01), where t starts from 0, ends at 0.99
    and then use np.sin and np.pi functions to genereate certain sine signals with certain
    frequencies. And remember the equation = sin(2*pi*f*t)
2) print 1 Hz sine signal to fig1
3) print 2 Hz sine signal to fig2
4) print 1,2,3,4 Hz sine signals to fig3 subplots. HINT: remember that axs is 2*2 matrix. 
   thus accessing second subplot goes with axs[0,1], where 0 = first row, 1 = second column.
5) print titles to all 3 figures
6) change line type and color of line of all 4 subplots at fig3 

7) And finally as we hopefully saw during the lectures that one can put
   many signals to a matrix and then just print matrix and all columns are
   seen as separate signals. Make signal matrix where you have a 1 second 2 Hz sine
   signal and its second power. And print those to a same figure.

'''

t = np.arange(0,1,0.01)
pii = np.pi
one = np.sin( 2 * pii * 1 * t) 
two = np.sin( 2 * pii * 2 * t) 
three = np.sin( 2 * pii * 3 * t) 
four = np.sin( 2 * pii * 4 * t)

fig1 = plt.figure("Figure 1")
fig1.suptitle('1Hz Signal')
plt.plot(t, one)

fig2, ax = plt.subplots()
fig2.suptitle('2Hz Signal')
ax.plot(t, two)

fig3, axs = plt.subplots(2,2)    
fig3.suptitle('Signals')

axs[0,0].set_title('1Hz')
axs[0,0].plot(t, one, '-.', color='red')

axs[0,1].set_title('2Hz')
axs[0,1].plot(t, two, '-.', color='green')

axs[1,0].set_title('3Hz')
axs[1,0].plot(t, three, '-.', color='blue')

axs[1,1].set_title('4Hz')
axs[1,1].plot(t, four, '-.', color='gray')



#Yksi tapa tehdä seiska kohta
SignalMatrix = np.zeros((100,2))
SignalMatrix[:,0] = two
SignalMatrix[:,1] = np.power(two,2)
fig4 = plt.figure("Matrix")
fig4.suptitle('2Hz Matrix Signal')
plt.plot(SignalMatrix)


#Toinen tapa tehdä seiska kohta
SignalMatrixT = np.matrix([two, np.power(two,2)])
fig5 = plt.figure("Matrix (Transpose)")
fig5.suptitle('2Hz Matrix Signal Using Transpose')
plt.plot(np.transpose(SignalMatrixT))


plt.show()


