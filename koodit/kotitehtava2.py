import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

""" 
Tehtävä 1: 
- lataa Latest https://covidtracking.com/data/download/national-history.csv
  tiedosto pandas kirjaston avulla Pandas dataframeksi. 
- "Irroita" siitä ladattaessa'date','deaths','hospitalInc','hospitalNow' sarakkeet
- Piirrä matplotlib.pyplot kirjaston ja plt.subplot, plt.plot, plt.title, plt.show 
  komentojen avulla kuva, josta nähdään kuolleiden lukumäärät, sairaalapotilaiden
  inkrementaalinen kasvu ja kuinka paljon sairaalassa on potilaita eri päivinä.
- Selvitä minä päivänä potilaiden kasvu on ollut suurinta ja mikä on tuon päivän potilasmäärä

Tehtävä 2:
- Muuta kaikki dataFramen sarakkeet numpy arrayksi to_numpy() funktion avulla
- Tulosta kuolleiden määrä ja sairaalassa olleiden lukumäärät oikeassa järjestyksessä
  (huom päivämäärät ovat tiedostossa viimeisin päivämäärä ensin. Eli käännä tulostusjärjestys
   siten, että kuvaan tulostetaan deaths sarakkeen viimeisin alkio ensin jne.)
""" 



def teht1():
    df = pd.read_csv('national-history.csv')
    print("Size of dataframe: ", df.shape)
    data = df[['date', 'death', 'hospitalizedIncrease', 'hospitalizedCurrently']]
    
    fig, ax = plt.subplots(3)

    ax[0].set_title('Dead')
    ax[0].plot(mdates.num2date(mdates.datestr2num(data['date'])),data['death'], color='red')

    ax[1].set_title('Hospitalized Increase')
    ax[1].plot(mdates.num2date(mdates.datestr2num(data['date'])),data['hospitalizedIncrease'], color='green')

    ax[2].set_title('Hospitalized Currently')
    ax[2].plot(mdates.num2date(mdates.datestr2num(data['date'])), data['hospitalizedCurrently'], color='blue')

    print(data[['date','hospitalizedIncrease']][data.hospitalizedIncrease==data['hospitalizedIncrease'].max()]) #Tulostaa päivän milloin potilaiden kasvu oli suurinta




def teht2():
    df = pd.read_csv('national-history.csv')
    date_array = df['date'].to_numpy()
    death_array = df['death'].to_numpy()
    Hosp_array = df['hospitalizedIncrease'].to_numpy()
    HospCur_array = df['hospitalizedCurrently'].to_numpy()
    date_array = date_array[::-1]
    death_array = death_array[::-1]
    Hosp_array = Hosp_array[::-1]
    HospCur_array = HospCur_array[::-1]

    date_array = mdates.num2date(mdates.datestr2num(date_array))
    
    fig, ax = plt.subplots(3)
    
    ax[0].set_title('Dead')
    ax[0].plot(date_array,death_array, color='red')

    ax[1].set_title('Hospitalized Increase')
    ax[1].plot(date_array,Hosp_array, color='green')

    ax[2].set_title('Hospitalized Currently')
    ax[2].plot(date_array, HospCur_array, color='blue')
    
    
    


    

teht1()
teht2()

plt.show()