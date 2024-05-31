import image_util
import os
import numpy as np
from skimage.draw import *

def check(x,y,height_sub,width_sub):
    for v in range(height_sub):
        for w in range(width_sub):
            f_xy = image[x+v, y+w]
            if f_xy != subimage[v, w]:
                return False
    return True


def register(image, subimage):
    height_img = image.shape[0]
    width_img = image.shape[1]
    height_sub = subimage.shape[0]
    width_sub = subimage.shape[1]

    for x in range(height_img-height_sub):
        for y in range(width_img-width_sub):
            f_xy = image[x, y]
            if f_xy == subimage[0, 0]:
                if check(x, y, height_sub, width_sub):
                    x_reg = x
                    y_reg = y
                    result = np.copy(image)
                    rr, cc = rectangle_perimeter((x_reg, y_reg),
                                                 end=(x_reg + subimage.shape[0], y_reg + subimage.shape[1]))
                    result[rr, cc] = 255
                    image_util.show(result)
                    break

BASE_DIRECTORY = '/Users/anne/PycharmProjects/Semester3/images'
image = image_util.read(os.path.join(BASE_DIRECTORY, 'level1_fix.png'), as_gray=True)
subimage = image_util.read(os.path.join(BASE_DIRECTORY, 'level1_sub.png'), as_gray=True)

register(image,subimage)

