import image_util
import os

def Aufgabe23():
    def compute_histogram(image): #nullen sind intensitätswerte, deren Häufigkeiten bestimmt werden sollen
        height = image.shape[0] #erzeugt Bild
        width = image.shape[1]
        histogram = [0] * 256 #Liste mit 265 mal 0

        for i in range(height): #durchläuft Bildhöhe
            for j in range(width): #durchläuft Breite
                f_xy = image[i, j] #bestimmt Pixelintensität jedes pixels durch durchlaufen der schleifen
                histogram[f_xy] += 1 #setzt für bestimmte Pixelintensität eine 1 in die Liste ein und addiert eine weitere 1 dazu,
        print(histogram)             #wenn dieser pixelwert nochmal erreicht wird, so wird die Häufigkeit bestimmt

    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
    image = image_util.read(os.path.join(BASE_DIRECTORY, 's_level2_krebsmetastasen_lcn.png'), as_gray=True)
    compute_histogram(image)
Aufgabe23()


def Aufgabe33():
    def Bildhelligkeit(image):
        height = image.shape[0]
        width = image.shape[1]

        for i in range(height): #durchläuft Bildhöhe
            for j in range(width): #durchläuft Bildbreite
                f_xy = 1.5 * image[i,j] #jede pixelintensität wird um 50% erhöht durch Multiplikation mit 1,5
                image[i, j] = min(f_xy, 255) #maximale intensität wird auf 255 beschränkt
        image_util.show(image)

    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
    image = image_util.read(os.path.join(BASE_DIRECTORY, 'mri-2.png'), as_gray=True)
    Bildhelligkeit(image)
Aufgabe33()
