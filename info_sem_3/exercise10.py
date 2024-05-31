import os
import numpy as np
import image_util

def aufgabe101():
    def fuse_images_impuls(images):
        height = image.shape[0]               #erstellt Ausgangsbild
        width = image.shape[1]
        target = np.zeros_like(image)         #erstellt Zielbild

        for x in range(height):               #durchläuft jeden Pixel des Bildes
            for y in range(width):
                sum = 0                       #definiert variable 'Sum' zu späteren Berechnung
                for i in range(len(images)):  #durchläuft die länge der Liste Images also alle darin enthaltenen Bilder
                    f_xy = (images[i])[x,y]   #nimmt den pixelwert eines bildes aus der liste
                    sum += f_xy               #addiert den pixelwert auf die summe auf
                m = sum // (len(images))      #berechnet Mittelwert der pixel der untersch. Bilder an Stelle x,y
                target[x,y] = m               #trägt den Mittel-Pixelwert ins Target an der entsprechenden Stelle

        image_util.show(target)

    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images/TarsusREM_part1&2'
    images = []
    for i in range(64):                                #durchläuft alle bilder des ordners
        name = 'TarsusREM_series_' + str(i) + '.jpg'   #untersch. Bilder haben unterschiedliche Namen
        image = image_util.read(os.path.join(BASE_DIRECTORY, name), as_gray=True)
        images.append(image)                           #fügt die einzelnen Bilder in eine Liste ein

    fuse_images_impuls(images)
aufgabe101()