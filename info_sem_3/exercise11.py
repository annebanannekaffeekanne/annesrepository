import os
import numpy as np
import image_util


def Kontrastoptimierung(target):
    height = target.shape[0]
    width = target.shape[1]
    a = 255  # legt a auf den Maximalwert fest
    b = 0  # legt b auf den Minimalwert fest

    for i in range(height):  # durchläuft Bildhöhe
        for j in range(width):  # durchläuft Bildbreite
            f_xy = target[i, j]  # bestimmt Pixelintensität der einzelnen Pixel
            a = min(f_xy, a)  # gibt den niedrigsten Wert aus
            b = max(f_xy, b)  # gibt den höchsten Wert aus

    for i in range(height):
        for j in range(width):
            f_xy = target[i, j]  # bestimmt Pixelintensität jeden Pixels
            target[i, j] = 255 * (f_xy - a) / (b - a)  # setzt neue Pixelintensität
    print(a, b)


def aufgabe111():
    def quadranten_min_koordinaten():
        height = image.shape[0]                   #erstellt Ausgangsbild
        width = image.shape[1]

        a = 255
        for x in range(0, int(height/2)):         #Quadrant I
            for y in range(0, int(width/2)):
                f_xy1 = image[x,y]                #bestimmt Pixelintensität an Stelle x,y
                a = min(f_xy1, a)                 #Variable a ist der minimale Pixelwert im Quadranten
                if f_xy1 == a:                    #wenn der minimale Pixelwert dem von f_xy entspricht...
                    print(x,y)                    #print die Koordinaten dieses Pixels
        print("der erste Pixelwert beträgt:", a)

        a = 255                                   #setze a wieder aus 255, damit es nicht den obigen Wert übernimmt
        for x in range(0, int(height/2)):         #Quadrant II (siehe Quadrant I)
            for y in range(int(width/2), width):
                f_xy2 = image[x,y]
                a = min(f_xy2, a)
                if f_xy2 == a:
                    print(x,y)
        print("der zweite Pixelwert beträgt:", a)

        a = 255
        for x in range(int(height/2), height):    #Quadrant III (siehe Quadrant I)
            for y in range(0, int(width/2)):
                f_xy3 = image[x,y]
                a = min(f_xy3, a)
                if f_xy3 == a:
                    print(x,y)
        print("der dritte Pixelwert beträgt:", a)

        a = 255
        for x in range(int(height/2), height):    #Quadrant IV (siehe Quadrant I)
            for y in range(int(width/2), width):
                f_xy4 = image[x,y]
                a = min(f_xy4, a)
                if f_xy4 == a:
                    print(x,y)
        print("der vierte Pixelwert beträgt:", a)

    def background_draw():
        height = image.shape[0]                             #erstellt Ausgangsbild
        width = image.shape[1]
        target = np.zeros_like(image)                       #erstellt Zielbild

        for x in range(height):
            for y in range(width):
                f_xy = image[x,y]                           #bestimmt Pixelintensität an der Stelle x,y
                value = f_xy - (10 + 0.137 * x + 0.097 * y) #bestimmt den neuen Wert des Hintergrundpixels
                if value < 0:                               #stellt sicher, dass keine negativen Werte berechnet werden
                    value = 0
                target[x,y] = value                         #fügt den neuen Pixelwert in das Zielbild ein
        Kontrastoptimierung(target)                         #wendet Methode Kontrastoptimierung an
        image_util.show(target)

    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
    image = image_util.read(os.path.join(BASE_DIRECTORY, 'fluo_shading.png'), as_gray=True)
    quadranten_min_koordinaten()
    background_draw()
aufgabe111()
