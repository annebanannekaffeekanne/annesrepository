import image_util
import os
import numpy as np
from math import*

def aufgabe121():
    def fuse_image(images, count_x, count_y):
        height = image.shape[0]
        width = image.shape[1]
        target = np.zeros_like(image)

        delta_x = height // count_x
        delta_y = width // count_y

        bildausschnitt = np.zeros((delta_x, delta_y))
        bildausschnitt2 = np.zeros((delta_x, delta_y))

        for block_x in range(count_x):  # Einteilung in Blöcke
            for block_y in range(count_y):
                start_x = block_x * (delta_x + 1)
                start_y = block_y * (delta_y + 1)
                end_x = (block_x + 1) * delta_x
                end_y = (block_y + 1) * delta_y

                var = 0
                for k in range(len(images)):
                    sum = 0
                    sum2 = 0
                    for i in range(start_x, end_x):  # durchlaufen der blöcke und bestimmen der varianz dieser
                        for j in range(start_y, end_y):
                            f_xy = image[i, j]
                            bildausschnitt2[i - start_x, j - start_y] = f_xy
                            sum += f_xy
                            sum2 += (f_xy ** 2)
                    m_quadrat = (sum / (height * width)) ** 2
                    sigma = (sum2 / (height * width))
                    varianz = sqrt(sigma - m_quadrat)  # bestimmte varianz
                    if varianz > var:
                        bildausschnitt = bildausschnitt2
                        var = varianz
                for i in range(start_x, end_x):  # durchlaufen der blöcke und bestimmen der varianz dieser
                    for j in range(start_y, end_y):
                        target[i, j] = bildausschnitt[i - start_x, j - start_y]

        image_util.show(target)

    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images/muecke_small'
    images = []
    for i in range(9):                                                    #durchläuft alle bilder des ordners
        name = 'muecke_small_' + str(i) + '.jpg'                          #untersch. Bilder haben unterschiedliche Namen
        image = image_util.read(os.path.join(BASE_DIRECTORY, name), as_gray=True)
        images.append(image)                                              #fügt die einzelnen Bilder in eine Liste ein

    fuse_image(images, 5, 4)
aufgabe121()