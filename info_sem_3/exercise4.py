import image_util
import os


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


BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
image = image_util.read(os.path.join(BASE_DIRECTORY, 's_level1_herzgewebe_lc.png'), as_gray=True)
Kontrastoptimierung(image)
BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
image = image_util.read(os.path.join(BASE_DIRECTORY, 's_level2_krebsmetastasen_lcn.png'), as_gray=True)
Kontrastoptimierung(image)
