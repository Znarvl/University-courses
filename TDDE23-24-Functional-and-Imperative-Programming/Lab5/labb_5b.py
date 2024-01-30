"""
Simon Jakobsson, Viktor Andersson U1A
"""

import math

def calc(x,y):

    """
    Använder oss av negativ gaussisk blur formeln samt
    tar in x och y som hänvisar till positionen från origo.
    Returnar beräkningen av formeln såvida x,y inte är 0
    """

    s = 4.5
    if x == 0 and y == 0:
        return 1.5
    else:
        gaussform  = -((x**2)+(y**2))/(2*s**2)
        return -(1/(2*math.pi*s**2))*math.e**gaussform


def unsharp_mask(n):

    """
    Tar in ett värde n för att få fram ett värde
    på alla x och y värden. Loopar igenom alla kombinationer
    av dessa och läggertil beräkning av gaussformeln i lista
    som returnas.
    """

    #Listbyggare som returnar alla x eller y värden
    minus = -(n//2)
    lista_n = [i + 1 for i in range((minus -1),(n + minus -1))]


    minus = lista_n[0]
    plus = lista_n[-1]

    #Listbyggare som returnar alla beärkningar av gaussformeln
    lista_a = [[calc(y,x) for x in range(minus,plus+1)] for y in range \
    (minus,plus+1)]

    return lista_a

print(unsharp_mask(3))
print(N(4))
