from func import *
import cv2
from cvlib import *


def gradient_condition(tup):
    """
    Tar in en tuple som representerar en pixel i en gråskala.
    returnar första värdet i tupeln(alla har samma värde)
    dividerat med högsta färgvärdet(alltså ett tal mellan 0-1)
    """

    return tup[0]/255



plane_img = cv2.imread("plane.jpg")
flower_img = cv2.imread("flowers.jpg")
gradient_img = cv2.imread("gradient.jpg")

plane_list = cvimg_to_list(plane_img)
flower_list = cvimg_to_list(flower_img)
gradient_list = cvimg_to_list(gradient_img)

generator1 = generator_from_image(plane_list)
generator2 = generator_from_image(flower_list)
gradient = generator_from_image(gradient_list)



def combine_images(hsv_list,gradient, generator1, generator2):
    """
    Använder oss av formeln vi fick i instruktionerna för att få fram
    en ny pixel
    """

    new_list=[]
    for i in range(len(hsv_list)):
        r = generator1(i)[2]*gradient_condition(gradient(i))
        g = generator1(i)[1]*gradient_condition(gradient(i))
        b = generator1(i)[0]*gradient_condition(gradient(i))

        r2 = generator2(i)[2]*(1-gradient_condition(gradient(i)))
        g2 = generator2(i)[1]*(1-gradient_condition(gradient(i)))
        b2 = generator2(i)[0]*(1-gradient_condition(gradient(i)))

        r = (r + r2)
        g = (g + g2)
        b = (b + b2)

        new_list.append((b,g,r))
    return new_list

hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
result=combine_images(hsv_list,gradient,generator1,generator2)
new_img = rgblist_to_cvimg(result, flower_img.shape[0], flower_img.shape[1])
cv2.imshow('combi',new_img)
cv2.waitKey(0)
