"""
Simon Jakobsson U1A
"""
"""
Gör en funktion till varje boolean vi kan ta
"""
def if_and(exp_if1, exp_if2):
    """
    and = båda statements måste vara true, hence
    den itererar bool2 över bool1
    """
    if exp_if1 == "true":
        if exp_if2 == "true":
            return "true"
    return "false"
def if_or(exp_or1, exp_or2):
    """
    if = om någon av påstående 1 eller 2 är true
    """
    if exp_or1 or exp_or2 == "true":
        return "true"
    return "false"


def if_not(exp):
    if exp == "true":
        return "false"
    return "true"

def interpret(exp, dict):
    #Tittar om exp är sträng
    if isinstance(exp, str):
        if exp == "true" or exp == "false":
            return exp
        else:
            #går igenom exp list
            return dict[exp]

    elif exp[1] == "AND":
            return if_and(interpret(exp[0], dict),interpret(exp[2], dict))
    elif exp[1] == "OR":
            return if_or(interpret(exp[0], dict), interpret(exp[2], dict))
    elif exp[0] == "NOT":
            return if_not(interpret(exp[1], dict))



print(interpret(["NOT", ["NOT", ["NOT", ["cat_asleep", "OR", ["NOT", "cat_asleep"]]]]],
               {"cat_asleep": "false"}))
