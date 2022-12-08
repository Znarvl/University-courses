"""
itererar över designerade bokstäver och tecken
lägger till i designerad variabel och returnerar ett output
går ej att lägga inom fuktionen
"""
def split_it(seq):

    lower, upper = "", ""
    #ger små bokstäver och tecken, lägger till i lower
    for char in seq:
        if char.islower() or char == "_" or char == ".":
            lower += char
        # om stora och tecken lägg till i upper
        elif char.isupper() or char == " " or char == "|":
            upper += char
    #returnar först lower och sedan upper
    return lower, upper


"""
Rekursivt
använder oss av element
går igenom baklänges så man ordnar upp listan så det faller rätt
delar upp bokstäver så de hamnar rätt genom olika krav
"""
def split_rec(seq):
    #om strängen är tom
    if seq =="":
        #sätter vid nästa ord
        return ("","")

#seq[0] retunerar små bokstäver + tecken
    if seq[0].islower() or seq[0] == "_" or seq[0] == ".":
        res = split_rec(seq[1:])
        #lägger till i första men inte andra
        return  seq[0] + res[0], res[1]

    #samma princip men stora bokstäver + tecken
    elif seq[0].isupper() or seq[0] == " " or seq[0] == "|":
        #går igenom funktionen, tar bort första bokstav då den anser att den är tom annars
        res = split_rec(seq[1:])
        return res[0], seq[0] + res[1]
    res = split_rec(seq[1:])
    return res

print(split_rec("hTEeSj_CO"))
