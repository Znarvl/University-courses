from func import *
import cv2
import random
from cvlib import *


def combine_images(hsv_list, condition, generator1, generator2):
    """
    Tar in hsv_list och tittar vilka element i hsv_list
    som uppfyller condition(vilket är gränsvärden)
    Om elementet uppfyller kraven
    tilldelas elementet i värdet från generator1(stjärnhimel),
    stämmer inte vilkoret sätts elementet till generator2(ordinarie bild)
    Returnar den nya överskrivna listan av
    hsv_list(destruktiv funktion)
    """

    for i in range(len(hsv_list)):
        if condition(hsv_list[i]) == 1:
            hsv_list[i] = generator1(i)
        else:
            hsv_list[i] = generator2(i)
    return hsv_list




plane_img = cv2.imread("plane.jpg")

condition = pixel_constraint(100, 150, 50, 200, 100, 255)

hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))

plane_img_list = cvimg_to_list(plane_img)

def generator1(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)

generator2 = generator_from_image(plane_img_list)

result = combine_images(hsv_list, condition, generator1, generator2)
new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])

cv2.imshow('Final image', new_img)

cv2.waitKey(0)
