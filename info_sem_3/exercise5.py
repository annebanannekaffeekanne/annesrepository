import image_util
import os
import numpy as np

def Aufgabe53():
    def apply_boxfilter(source, a):
        height = source.shape[0]
        width = source.shape[1]
        target = np.zeros_like(source)         #erzeugt ein schwarzes Bild, in der gleichen Form wie das Bild source
        source = np.pad(source,(a,a))          #zero padding mit a als Umgebung
        maske = (2*a+1) * (2*a+1)              #erstellen der Filtermaske

        for i in range(height):                #durchlaufen des Bildes
            for j in range(width):
                sum = 0                        #erstellen der Variablen Summe, um pixelwerte folgend aufzuaddieren
                for k in range(i-a, i+a+1):    #Filtermaske auf Bild legen und von oberer zur unteren Ecke durchlaufen
                    for l in range(j-a,j+a+1):
                        f_xy = source[k,l]     #pixelwert an bestimmter Stelle bestimmen und in Variable speichern
                        f_xy *= 1 / maske      #verändert intensitätswert mittels Filtermaske (faktor: 1/maske)
                        sum += int(f_xy)       #addiert veränderte pixelwerte auf
                        target[i,j] = sum      #weist den pixelwert 'summe' dem entsprechenden Pixel des neuen Bilds zu

        image_util.show(source)
        image_util.show(target)

    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
    source = image_util.read(os.path.join(BASE_DIRECTORY, 'zellen_ld.png'), as_gray=True)
    apply_boxfilter(source, 3)
Aufgabe53()