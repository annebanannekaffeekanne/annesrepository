import image_util
import os
import numpy as np

def aufgabe113():
    def microarray_beschneiden():
        height = image.shape[0]
        width = image.shape[0]
        #target = image((height, width, 4), dtype=np.uint8)

        for x in range(height):
            for y in range(width):
                f_xy = image[x, y]
                if f_xy < 240:
                    print(x-1)
                    break

        for y in range(width):
            for x in range(height):
                f_xy = image[x, y]
                if f_xy < 240:
                    print(y-1)
                    break





    BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
    image = image_util.read(os.path.join(BASE_DIRECTORY, 'tissue_microarray_1.jpg'), as_gray=False)
    microarray_beschneiden()

aufgabe113()