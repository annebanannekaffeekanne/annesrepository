#Aufgabe 2
import image_util
import os
from math import*
def aufgabe22():
    def compute_mean(image):
        height = image.shape[0]
        width = image.shape[1]
        sum = 0
        for i in range(height):       #durchlaufen des Bildes
            for j in range(width):
                f_xy = image[i, j]    #pixelwert der entsprechenden Stelle als Variable speichern
                sum += f_xy           #summe um Pixelwert erhöhen --> summe aller pixelwerte bestimmen
        m = sum / (height * width)    #mittelwert berechnen, indem summe aller intensitäten durch gesamtpixelzahl dividiert wird
        print(m)

    def compute_var(image):
        height = image.shape[0]
        width = image.shape[1]
        sum = 0
        sum2 = 0
        # mittelwert = compute_mean(image)
        for i in range(height):
            for j in range(width):
                f_xy = image[i, j]                #Pixelwert an Stelle bestimmen
                sum += f_xy                       #pixelwerte aufaddieren (Intensitäten)
                sum2 += (f_xy**2)                 #jeden Pixelwert quadrieren und Summe aller werte bilden
        m_quadrat = (sum / (height * width))**2   #Mittelwert berechnen und quadrieren
        sigma = (sum2/(height * width))           #quadrierte pixelwerte durch Gesamtpixelzahl dividieren
        varianz = sqrt(sigma - m_quadrat)         #wurzel aus Differenz von sigma und m
        print(varianz)

    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
    image = image_util.read(os.path.join(BASE_DIRECTORY,'s_cancer.png'),as_gray=True)
    compute_mean(image)
    compute_var(image)
    image = image_util.read(os.path.join(BASE_DIRECTORY,'s_cancer_blur.png'),as_gray=True)
    compute_mean(image)
    compute_var(image)
aufgabe22()




def zusatz():

    def Blockgliederung(image):
        height = image.shape[1]
        width = image.shape[1]

        for i in range(0, height, 8):              #durchwandert Bildhöhe in achter Schritten
            for j in range(0, width, 8):           #durchwandert Bildbreite in achter Schritten
                f_xy = image[i, j]                 #bestimmt Pixelintensität an der Stelle x,y
                for k in range(8):                 #durchläuft acht pixel
                    for l in range(8):
                        image[i + k, j + l] = f_xy #malt kleine 8x8 Blöcke mit entsprechender Farbintensität aus


        image_util.show(image)

    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
    image = image_util.read(os.path.join(BASE_DIRECTORY, 'mri-2.png'), as_gray=True)
    Blockgliederung(image)
zusatz()