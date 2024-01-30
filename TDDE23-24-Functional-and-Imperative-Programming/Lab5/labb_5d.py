import cv2
import numpy as np
from cvlib import *



def generator_from_image(list_img):
    """
    Tar in en lista med tuples där varje tuple representerar
    en pixel och returnar funktionen pixel
    """
    

    def pixel(index):
        """
        Tar in ett indexvärde och returnar tupeln som
        har det indexvärdet
        """

        return list_img[index]

    return pixel


def cvimg_to_list(im):
    """
    Tar in en bild och returnar en lista bestående
    av tuples där varje tuple representerar en pixels bgr värde
    """

    height = im.shape[1]
    width = im.shape[0]
    list_pixel = []

    #Itererar genom hela bilden (x,y)
    for x in range(0,width):
        for y in range(0,height):
            pixel = im[x,y]
            #BRG element
            blue = pixel[0]
            green = pixel[1]
            red = pixel[2]
            list_pixel.append((blue,green,red))

    return list_pixel
