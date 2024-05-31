import image_util
import os
import numpy as np


def Kontrastoptimierung(image):
    height = image.shape[0]
    width = image.shape[1]
    a = 255 #legt a auf den Maximalwert fest
    b = 0 #legt b auf den Minimalwert fest

    for i in range(height): #durchläuft Bildhöhe
        for j in range(width): #durchläuft Bildbreite
            f_xy = image[i, j] #bestimmt Pixelintensität der einzelnen Pixel
            a = min(f_xy, a) #gibt den niedrigsten Wert aus
            b = max(f_xy, b) #gibt den höchsten Wert aus

    for i in range(height):
        for j in range(width):
            f_xy = image[i, j] #bestimmt Pixelintensität jeden Pixels
            image[i, j] = 255 * (f_xy - a) / (b-a) #setzt neue Pixelintensität
    print(a, b)
    image_util.show(image)

def aufgabe62():
    def multichannel_image(image_c0, image_c1, image_c2):
        target = np.zeros((512, 512, 3), dtype=np.uint8)  #erstellt schwarzes Zielbild (gleiche Größe wie Channels)
        Kontrastoptimierung(image_c0)                     #führt die Methode Kontrastoptimierung an den
        Kontrastoptimierung(image_c1)                     #3 Bildern durch
        Kontrastoptimierung(image_c2)

        height = target.shape[0]
        width = target.shape[1]

        for i in range(height):                           #durchläuft das Zielbild und die channel bilder
            for j in range(width):
                f_xy = image_c0[i,j]                      #speichert Pixelwerte der verschiedenen Channel an der
                g_xy = image_c1[i,j]                      #gleichen Position i,j
                h_xy = image_c2[i,j]
                target[i,j] = (g_xy, h_xy, f_xy)          #jeder Channel ist einem Farbkanal zugeordnet; die Pixelwerte
                                                          #werden der entsprechenden Farbe im Zielbild zugeordnet
        image_util.show(target)

    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
    image_c0 = image_util.read(os.path.join(BASE_DIRECTORY, 'channel0.png'), as_gray=True)
    image_c1 = image_util.read(os.path.join(BASE_DIRECTORY, 'channel1.png'), as_gray=True)
    image_c2 = image_util.read(os.path.join(BASE_DIRECTORY, 'channel2.png'), as_gray=True)
    multichannel_image(image_c0, image_c1, image_c2)

aufgabe62()