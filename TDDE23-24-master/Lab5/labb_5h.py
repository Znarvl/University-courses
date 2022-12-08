def generator_from_image(list_img):
    """
    Takes tupel with bgr info of image, function will be used
    as for information
    """


    def pixel(i):
        """
        returns BGR info about pixel
        """

        try:
            return list_img[i]
        except TypeError:
            print("generator_from_image IndexError")
            raise
        except IndexError:
            print("generator_from_image type error")
            raise
        except:
            print("generator_from_image något annat gick fel")
            raise


    return pixel


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """
    recieves hue, saturation and value, from low to high, creates
    contraint that is stored in function
    """


    def is_hsv(hsv):
        """
        Checks the values is within the values of high and low,
        if it is, returns 1, if not it returns 0
        """

        try:
            if hsv[0] >= hlow and hsv[0] <= hhigh and hsv[1] >= slow  \
            and hsv[1] <= shigh and hsv[2] >= \
            vlow and hsv[2] <= vhigh:
                return 1
            else:
                return 0
        except TypeError:
            print("pixel_constraint TypeError")
            raise
        except IndexError:
            print("pixel_constraint IndexError")
            raise
        except:
            print("pixel_constraint något annat gick fel")
            raise


    return is_hsv


def combine_images(hsv_list, condition, generator1, generator2):
    """
    Takes in a list, filter and two generators(images)
    if pixel is within correct filter requirements, new pixel
    is generated. Combined the new pixels are stored in a new
    list which will be displayed as new image
    """

    try:
        for i in range(len(hsv_list)):
            if condition(hsv_list[i]) == 1:
                hsv_list[i] = generator1(i)
            else:
                hsv_list[i] = generator2(i)
        return hsv_list
    except LookupError:
        print("combine_images LookupError")
        raise
    except IndexError:
        print("combine_images IndexError")
        raise TypeError
    except:
        print("combine_images something else went wrong")
        raise



def test_generator_from_image():
    """
    Testing that the correct output is recieved,
    if not, it will output an Error that will be printed
    """

    img = [(12,32,12),(123,54,2),(123,43,54),(10,32,143)]
    test = generator_from_image(img)
    try:
        test((1200))
    except IndexError:
        print("TypeError as expected test_generator_from_image")
    except:
        print("Something went wrong test_generator_from_image1")
        raise
    else:
        print("No error occured test_generator_from_image1")
    try:
        test(("viktor gillar korv"))
    except TypeError:
        print("TypeError as expected generator from image")
    except:
        print("Something went wrong generator from image")
        raise
    else:
        print("No error occured test_generator_from_image2")


def test_pixel_constraint():
    """
    Testing that the correct output is recieved,
    if not, it will output an Error that will be catched
    """

    test = pixel_constraint(50,100,25,100,60,120)
    try:
        test(())
    except IndexError:
        print("IndexError in pixel contraint")
    except:
        print("Something went wrong pixel contraint")
        raise
    else:
        print("No error occured test_pixel_constraint1")

    try:
        test(("Skit"))
    except TypeError:
        print("TypeError in pixel constraint")
    except:
        print("Something else went wrong pixel constraint")
        raise
    else:
        print("no error occured test_pixel_constraint2")


def test_combine_images():
    """
    Testing that the correct output is recieved,
    if not, it will output an Error that will be catched
    """

    condition = pixel_constraint(50,100,25,100,60,12)
    constraint = condition(((120,45,2,50)))
    generator1 =  generator_from_image([(50,121,32),(100,3,33)])
    generator2 =  generator_from_image([])


    try:
        hsv_list = [(123,123,123123)]
        combine_images(hsv_list, condition, generator1, generator2)
    except LookupError:
        print("LookupError test_combine_images")
    except:
        print("något annat fungerade inte test_combine_images")
        raise
    else:
        print("No error occured test_combine_images1")

    try:
        hsv_list_index_error = ["lol", (123.5, 123.5, 123.5), \
        (0, 0, 0), (23 ,23 ,23)]
        combine_images(hsv_list_index_error, condition,\
        generator1, generator2)
    except TypeError:
        print("IndexError(TypeError) combine_images")
    except:
        print("något annat gick fel test_combine_images")
        raise
    else:
        print("No error occured test_combine_images2")


test_combine_images()
test_generator_from_image()
test_pixel_constraint()
