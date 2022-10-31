import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


'''
TEHTAVA 1: Python ja numpy perusteita

Tee numpy datamatriisi, jossa on 5 riviä ja 5 saraketta ja numerot 0,1,2,..,23,24 alla olevan
kuvan mukaisesti. Muokkaa tämän jälkeen matriisia siten, että kopioit ensimmäisen rivin viimeiseksi
ja viimeisen rivin ensimmäiseksi kuvan mukaisesti. Ja kaikki tämä pitää tehdä vähemmällä kuin 10 
koodirivillä. Eli ei lähdetä siirtämään alkioita yksitellen. Vihje: rivin tilapäistä tallentamista
varten rivi kannattaa kopioida talteen .copy() funktion avulla. 

[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]

[[20 21 22 23 24]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [ 0  1  2  3  4]]
'''
def tehtava1():
    #print("Tahan toteutetaan tehtava 1 aliohjelmana")
    dataMatrix = np.zeros((5,5))
    dataMatrix[0] = np.arange(0,5)
    dataMatrix[1] = np.arange(5,10)
    dataMatrix[2] = np.arange(10,15)
    dataMatrix[3] = np.arange(15,20)
    dataMatrix[4] = np.arange(20,25)
    temp = dataMatrix[0].copy()
    dataMatrix[0] = dataMatrix[4]
    dataMatrix[4] = temp
    print(dataMatrix)
    

'''
TEHTAVA 2: Python perusteet
Tee aliohjelma, joka
1. lukee parametrina annetun tiedostonimen mukaisen csv-tiedoston pandas dataframeen
2. Muuttaa dataframen x sarakkeen numpy arrayksi
3. Etsii pythonin for-luupin ja if komennon avulla y muuttujan datasta (vaikka tämä olisi numpyn avulla helpomminkin 
   tehtävissä, niin tässä tehtävässä data pitää kuitenkin käydä läpi for-luupin ja if lausekkeiden avulla) 
   ne paikat, joissa y-muuttujan arvo EI ole välillä 0  1023 ja muuttaa noiden virheellisten lukujen paikalle arvon 0
4 palauttaa x muuttujan alkioiden keskiarvon laskettuna korjatusta datasta.

Eli kun funktiota kutsutaan näin:
print("x-muuttujan keskiarvo = ",tehtava1('data.csv'))

niin tulos on ohjelma tulostaa seuraavan tuloksen:

x-muuttujan keskiarvo = 346.7

'''
def tehtava2(tiedostonimi):
    #print("ja tahan toteutetaan tehtava 2 aliohjelmana")
    df = pd.read_csv(tiedostonimi)
    data_array = df.to_numpy()
    lenght = np.shape(data_array)
    for i in range(lenght[0]):
        if(data_array[i] < 0 or data_array[i] > 1023):
            data_array[i] = 0
    return np.average(data_array)



'''
TEHTAVA 3:
Muuta tämä tiedosto sellaiseksi, että tiedoston lopussa olevat testikoodit
jätetään suorittamatta, jos tämä tiedosto ei ole pääohjelma.
Importtaa sen jälkeen tämä tiedosto paaohjelma.py tiedostossa siten, etta
annettu paaohjalma.py suorittaa kaikki tässä tiedostossa olevat aliohjelmat
oikein.

'''



'''
TEHTAVA 4:
Tee aliohjelma, joka on muotoa tehtava1(Fs,f,T,N), missä
Fs = näytetaajuus, olkoon se aliohjelmaa testattaessa 100,
f = suorakaide signaalin perustaajuus, olkoon se aliohjelmaa testataessa 1 Hz
t = aika sekuntteina ja olkoon tuo aliohjelmaa testattaessa 3 s
N = Siniaaltojen lukumäärä = 4, jotka aliohjelma laskee alla olevan kaavan mukaan

sin(2*pi*f*t) + 1/3*sin(3*2*pi*f*t) + 1/5*sin(5*2*pi*f*t)  + 1/7*sin(7*2*pi*f*t) (kaava 1)

sin funktio löytyy numpystä np.sin()
pi:n arvo löytyy myös numpystä np.pi

Esimerkkejä siitä, kuinka tehdään aika-akseli t np.arange -funktion avulla
ja kuinka tehdään tietyn taajuinen sinisignaali numpyn avulla löytyy
kurssin aikana annetuista opettajan esimerkeistä paljon.

Aliohjelman rakenne pitää olla seuraavanlainen:

1. Alusta muuttuja sig nolliksi np.zeros(N) funktion avulla, N = Fs*T 
2. Laske näyteväli Ts näytetaajuuden Fs käänteislukuna.
3. Muodosta aika-akseli t np.arange() funktion avulla.
4. Tee for luuppi, joka käy N-kierrosta ja jokaisella kierroksella:
    -lisää sig muuttujaan kaavan 1 mukaisen signaalin osan
    -printtaa sig muuttujaan summautuneen signaalin plt.subplot() komennolla
5. Ja lopuksi for luupin jälkeen tulostetaan neljään kuvaan tulleet kuvat plt.show()
'''
def tehtava4(Fs,f,t,N):
    #print("Tahan toteutetaan sitten tehtava 4 aliohjelmana")
    sig = np.zeros(N)
    Ts = 1/Fs
    t = np.arange(0,3,Ts)
    
    plt.figure(1)
    for i in range(N):
        num = (i+1)+i
        if i == 0:
            sig = (1/num)*np.sin(num*2*np.pi*f*t)
        else: 
            sig += (1/num)*np.sin(num*2*np.pi*f*t)
        plt.subplot(2,2,i+1)
        plt.plot(sig)
    plt.show()




'''
Tässä alla on koodia, jolla eri tehtävien toiminta voidaan testata
Muokkaa alla olevaa koodia tehtävän 3 suorituksessa siten, että näitä
testikoodeja ei suoriteta siinä tapauksessa, että tämä tiedosto ei ole ns.
pääohjelma.
'''
#print('Näilla alla olevilla komennoilla testataan toteutettuja aliohjelmia')
#tehtava1()
#print("x-muuttujan keskiarvo = ",tehtava2('data.csv'))
#tehtava4(100,1,3,4)
