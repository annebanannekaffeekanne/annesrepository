import image_util
import os
import numpy as np
from math import*

def aufgabe72():
    def rotate_forward(source, degree):
        height = source.shape[0]                                 #erstellt Bild
        width = source.shape[1]
        target = np.zeros((height, width, 3), dtype=np.uint8)    #erstellt schwarzes Zielbild

        bogen = (degree/180)*pi                                  #Umrechnung von Grad- in Bogenmaß

        for v in range(height):                                  #durchläuft Bild
            for w in range(width):
                f_vw = source[v,w]                               #nimmt Pixelwert an der Stelle v, w
                x = int(cos(bogen)*v-sin(bogen)*w)               #weist neue Koordinaten durch
                y = int(sin(bogen)*v+cos(bogen)*w)               #Transformation der Ausgangswerte zu
                if 0 <= x < height and 0 <= y < width:           #Bedingung, dass Bildhöhe und -breite nicht
                                                                 #überschritten werden
                    target[x,y] = (f_vw)                         #einfügen der neuen Koordinaten in das Zielbild


        image_util.show(target)


    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
    source = image_util.read(os.path.join(BASE_DIRECTORY, 'tannennadel.png'), as_gray=False)
    rotate_forward(source, 5)
aufgabe72()