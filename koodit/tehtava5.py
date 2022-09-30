'''
Install scikit-learn module with pip install scikit-learn command.

Tehtävät:
1. Luetaan dataout.csv tiedosto pandas data frameksi siten, että tiedostosta luetaan vai
   sarakkeet xyz ja labels. Eli jätetään se indeksi sarake, joka koostuu 0,1,2 jonosta pois. 
   Käytä dataframen read_csv funktiota ja sieltä parametreja delimiter=, header=, usecols=

2. Poistetaan edellä luetusta dataframesta sen ensimmäinen rivi, jossa siis xyz ja labels tieto.
   Tämä siksi, että jäljelle jäänyttä 60,3 matriisia ja string saraketta käytetään eri algoritmien
   opettamiseen. Käytä dataframe iloc metodia

3. Seuraavaksi suodatetaan dataframesta pois sellaiset rivit, joissa x,y tai z arvo on suurempi
   kuin 1023, mikä on Arduinon analogia muuntimen maksimi lukema. Eli poistetaan virheelliset 
   mittaustulokset. Tulosta dataframe rivistä 40 eteenpäin (iloc käsky) ennen suodatusta ja 
   suodatuksen jälkeen, jotta varmistut siitä, että osa riveistä poistuu suodatuksen avulla
   Selvitä internetin avulla kuinka pandas dataframen sarakkeen arvoja voi suodattaa.

4. Seuraavaksi irroitetaan dataframesta labels tiedot left, right, up ja down tietoja
   kertova sarake (sen pitäisi olla neljäs sarake. Voit kokeilla esim print(df[4]) komennolla)
   Muutetaan sarakkeen tyyppi as_type komennolla 'category' tyypiksi ja luodaan dataframeen
   vielä viides sarake ja alustetaan sinne df[4].cat.codes funktion avulla numeeriset arvot
   left, rigth, up ja down arvoja vastaamaan.

5. Seuraavaksi "irroitetaan" dataframesta x,y,z sarakkeet ja muodostetaan niistä yksi 
   NumPy array, jossa on kolme saraketta ja N kpl rivejä. Tämä array = matriisi = data on sitten
   se, mitä käytetään eri mallien datana opettamiseen. Irroitetaan myös numpy arrayksi
   se viides sarake joka edellisessä vaiheessa saatiin tehtyä. Ja tätä käytetään opetuksessa
   kertomaan, mitä kukin data matriisin rivi edustaa = labels. Ja muutetaan molemmat irroitetut
   data ja labels int tyyppisiksi.

6. Ja nyt vihdoin data on käsitelty algoritmin opettamiseen sopivaksi. Jaetaan data vielä
   training ja test datasetteihin ja käytetään siihen sklearn kirjaston train_test_split luokkaa
   jonka voi importata komennolla from sklearn.model_selection import train_test_split. Tee
   sellainen jako, että datasta 20% jätetään testaukseen ja 80% datasta käytetään opetukseen.
   Netistä löytyy taas hyviä esimerkkejä, miten tämä tehtään: https://realpython.com/train-test-split-python-data/

7. Ja lopuksi testataan random forest ja K-means algoritmien toimivuutta. Eli opetetaan opetusdatalla
   x_train,y_train sekä random forest että K-means malli. Ja sen jälkeen testataan mallin tarkkuus
   x_test,y_test datalla. Ja ylimääräisenä tehtävänä voi vielä mitata kummastakin algoritmista kuinka
   kauaan mallin opettaminen kestää ja kuinka kauan yhden ennustuksen tekeminen mallilla kestää. Ja
   apuja löytyy taas netistä seuraavasti:
   K-means: https://towardsdatascience.com/knn-using-scikit-learn-c6bed765be75
   Random Forests:https://www.datacamp.com/tutorial/random-forests-classifier-python

       
'''

from cProfile import label
from unicodedata import category
import sklearn # This is anyway how package is imported
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time


df = pd.read_csv('dataout.csv',delimiter='\t', header=None, usecols=[1,2,3,4])

df = df.iloc[1:, 0:4]
df = df.astype({1: int, 2: int, 3: int, 4: "category"})
df[5] = df[4].cat.codes
#print(df)

filt_df = df[(df[1] < 1024) & (df[2] < 1024) & (df[3] < 1024)]        #Suodatetaan yli 1023 rivit pois
#print(filt_df)

data_matrix = np.zeros((filt_df.shape[0],3),dtype=int)
data_matrix[:, 0] = filt_df[1].to_numpy()
data_matrix[:, 1] = filt_df[2].to_numpy()
data_matrix[:, 2] = filt_df[3].to_numpy()
#print(data_matrix)

label_array = np.zeros((filt_df.shape[0],1),dtype=int)
label_array = filt_df[5].to_numpy()
#print(label_array)


x_train, x_test, y_train, y_test = train_test_split(data_matrix,label_array, test_size=0.2)
#print(y_test)




'''
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
   max_depth=None, max_features='auto', max_leaf_nodes=None, min_impurity_split=1e-07, 
   min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0,
   n_estimators=40, n_jobs=1, oob_score=False, random_state=None, verbose=0, warm_start=False)
'''
#RandomForests
start =  time.time()

model = RandomForestClassifier(n_estimators=40)
model.fit(x_train, y_train)
print("Training time for random forests: ", (time.time()-start)*1000,"ms")
print('Random Forests accuracy: ', model.score(x_test, y_test))

y_predicted = model.predict(x_test)
cm = confusion_matrix(y_test, y_predicted)
print(cm)



#K-means
start = time.time()

model = KNeighborsClassifier(n_neighbors=4)
model.fit(x_train, y_train)
print("Training time for k-means: ", (time.time()-start)*1000,"ms")
print('K-means accuracy: ', model.score(x_test, y_test))

y_predicted = model.predict(x_test)
cm = confusion_matrix(y_test, y_predicted)
print(cm)