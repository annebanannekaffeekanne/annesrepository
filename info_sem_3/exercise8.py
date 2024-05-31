import image_util
import os
import numpy as np
from math import*

def aufgabe82():
    def rotate_inverse_center(source, degree):
        alpha = (degree / 180) * pi                              # Umrechnung von Grad- in Bogenmaß
        height = source.shape[0]                                 # erstellt Bild
        width = source.shape[1]
        target = np.zeros((height, width, 4), dtype=np.uint8)

        for x in range(height):
            for y in range(width):
                f_xy = source[x,y]                               #liest pixel intensität beim jeweiligen x,y

                #T1 (x-(height/2)) und (y-(width/2)): Verschiebung der Mittelpunktkoordinaten von source in den Nullpunkt
                #T2 (Versch*cos(-alpha) + sin(alpha)*Versch) und (Versch*sin(-alpha)+cos(alpha)*Versch)
                  #Rotation um angegebenen Winkel alpha
                #T3 rotation+(height/2) und rotation+(width/2) Zurückverschiebung des rotierten Bildes an die
                  #neuen Stellen im Target
                v = int((x-height/2)*cos(-alpha)-sin(-alpha)*(y-width/2)+(height/2))
                w = int((x-height/2)*sin(-alpha)+cos(-alpha)*(y-width/2)+(width/2))

                if 0 <= v < height and 0 <= w < width:
                    target[x, y] = f_xy

        image_util.show(target)
    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
    source = image_util.read(os.path.join(BASE_DIRECTORY, 's_tannennadel.png'), as_gray=False)
    rotate_inverse_center(source, 5)
aufgabe82()



def aufgabe8zusatz():
    def rotate_inverse_center2(source, degree):
        alpha = (degree / 180) * pi                              # Umrechnung von Grad- in Bogenmaß
        height = source.shape[0]                                 # erstellt Bild
        width = source.shape[1]
        target_height = int(height + 2.5 *(sin(-alpha) * (height/2))) #neue höhe/breite addiert auf alte die länge der
        target_width = int(width + 1.5 *(sin(-alpha) * (width /2)))   #Gegenkathete des entstandenen dreiecks hinzu
        target = np.zeros((height, width, 4), dtype=np.uint8)

        for x in range(height):
            for y in range(width):
                f_xy = source[x,y]                               #liest pixel intensität beim jeweiligen x,y

                v = int((x-height/2)*cos(-alpha)-sin(-alpha)*(y-width/2)+(target_height/2))#wie aufgabe82, nur dass
                w = int((x-height/2)*sin(-alpha)+cos(-alpha)*(y-width/2)+(target_width/2)) #rückverschiebung ins Target
                                                                                           #erfolgt, das andere maße hat
                if 0 <= v < target_height and 0 <= w < target_width:
                    target[x, y] = f_xy

        image_util.show(target)
    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
    source = image_util.read(os.path.join(BASE_DIRECTORY, 's_tannennadel.png'), as_gray=False)
    rotate_inverse_center2(source, 5)
aufgabe8zusatz()