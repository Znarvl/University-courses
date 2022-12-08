from func import  *
def test_pixel_constraint():
    """
    Testar funktionen pixel_contraint genom att mata in olika värden
    som testar om funktionen ger korrekta värden
    """

    #Översta gränsvärdet
    test_case1 = pixel_constraint(0,255,0,255,0,255)

    #Ett "random" värde
    test_case2 = pixel_constraint(20,100,10,150,5,20)

    #Lägsta gränsvärde
    test_case3 = pixel_constraint(0,1,0,1,0,1)

    # Max gränsvärde
    test_hsv1 = test_case1((255,255,255))
    assert test_hsv1 == 1

    #lumpat värde inom gränsen
    test_hsv2 = test_case2((50,120,10))
    assert test_hsv2 == 1

    #Lägsta värdet
    test_hsv3 = test_case3((0,0,0))
    assert test_hsv3 == 1

    #Över gränvärdet, kommer misslyckas
    test_hsvfail1 = test_case1((300,300,300))
    assert test_hsvfail1 == 0


    #Ogiltiga värden som går under gränsen
    test_hsvfail2 = test_case2((10,5,0))
    assert test_hsvfail2 == 0

    #Värdem som ligger över gränsen
    test_hsvfail3 = test_case3((10,10,10))
    assert test_hsvfail3 == 0

    print("All test passed pixel contraint")
test_pixel_constraint()


def test_generator_from_image():
    """
    Testar värden för pixlar, genom att gå igenom  listan med tupels
    så ser vi om de returnar korrekt tupel genom titta på elementen
    """

    #Tar in slumpad listar med 3 pixlar
    test_case = generator_from_image([(123,32,1),(3,1,5),(12,43,54)])

    #Kollar om pixel returnas i pixel funktionen
    test_pixel1 = test_case((0))
    assert test_pixel1 == (123,32,1)

    #KOllar om pixel 2 returnas i pixel funktionen
    test_pixel2  = test_case((1))
    assert test_pixel2 == (3,1,5)

    #Kollar om pixer 3 returnas i pixel funktionen
    test_pixel3 = test_case((2))
    assert test_pixel3 == (12,43,54)

    print("All tests passed generator")



test_generator_from_image()

def test_combine_images():
    """
    Testar funktionen combine_images genom att ta in olika värden av hsv
    och slumpar korrekta värden för condition generator1 och generator2
    """
    #Lägsta värde för hsv
    hsv1 = [(0,0,0),(0,0,0),(0,0,0)]

    #Slumpat värde för hsv
    hsv2 = [(12,100,30),(200,90,0),(30,50,0)]

    #Maxat värde för hsv
    hsv3 = [(255,255,255),(255,255,255),(255,255,255)]

    condition = pixel_constraint(0,100,0,50,0,120)
    generator1 = generator_from_image([(125,123,100),(50,20,80),(110,130,60)])
    generator2 = generator_from_image([(75,23,200),(150,203,87),(10,30,60)])


    test_case1 = combine_images(hsv1, condition, generator1, generator2)
    assert test_case1 == [(125,123,100),(50,20,80),(110,130,60)]


    test_case2 = combine_images(hsv2, condition, generator1, generator2)
    assert test_case2 == [(75,23,200),(150,203,87),(110,130,60)]


    test_case3 = combine_images(hsv3, condition, generator1, generator2)
    assert test_case3 == [(75,23,200),(150,203,87),(10,30,60)]

    print("All tests passed combined images")
test_combine_images()
