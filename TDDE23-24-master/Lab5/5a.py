"""
Simon Jakobsson, Viktor Andersson U1A
"""
import cv2
from cvlib import *

def cvimg_to_list(im):

    """
    Tar in en bild och returnar en lista bestående
    av tuples där varje tuple representerar en pixels bgr värde
    """

    height = im.shape[1]
    width = im.shape[0]
    list_pixel = []

    #Itererar genom alla pixar (x,y)
    for x in range(0,width):
        for y in range(0,height):
            pixel = im[x,y]
            #BRG då vi tittar igenom elementen
            blue = pixel[0]
            green = pixel[1]
            red = pixel[2]
            #Lägger till bgr i vår tomma lista
            list_pixel.append((blue,green,red))
    return list_pixel




img = cv2.imread('plane.jpg')
list_img = cvimg_to_list(img)
converted_img = rgblist_to_cvimg(list_img, img.shape[0], img.shape[1])
cv2.imshow("converted", converted_img)

cv2.waitKey(0)
