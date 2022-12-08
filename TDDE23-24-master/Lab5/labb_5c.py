"""
Simon Jakobsson, Viktor Andersson U1A
"""
import cv2
import numpy as np
from cvlib import *


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """
    Tar in parametrar för gränsvärden till hsv
    """


    def is_hsv(hsv):
        """
        Kollar om hsv ligger innanför gränserna
        """

        if hsv[0] >= hlow and hsv[0] <= hhigh and hsv[1] >= slow and hsv[1] \
        <= shigh and hsv[2] >= vlow and hsv[2] <= vhigh:
            return 1
        else:
            return 0

    return is_hsv


def cvimg_to_list(im):
    """
    Räknar ut pixlarna i en tupel
    """

    height = im.shape[1]
    width = im.shape[0]
    list_pixel = []

    #Itererar genom hela bilden (x,y)
    for x in range(0,width):
        for y in range(0,height):
            pixel = im[x,y]
            #BGR element
            blue = pixel[0]
            green = pixel[1]
            red = pixel[2]
            list_pixel.append((blue,green,red))

    return list_pixel


hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
plane_list = cvimg_to_list(hsv_plane)
is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))
cv2.imshow('sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0],
hsv_plane.shape[1]))
cv2.waitKey(0)
