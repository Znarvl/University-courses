def interpret(exp, dict):
    #Tittar om exp är sträng, annars lista
    if isinstance(exp, str):
        #går igenom om exp ligger i dict
        if exp in dict:
            return dict[exp]
        return exp
    #tittar var elementet ligger och går igenom funktion för varje funktionskallesle rekursivt
    if len(exp) = 3:
        if exp[1] == "AND":
                return "true" if interpret(exp[0], dict) == "true"  and interpret(exp[2], dict) == "true" else "false"
        elif exp[1] == "OR":
                return "true" if interpret(exp[0], dict) == "true" or interpret(exp[2], dict) =="true" else "false"
    elif len(exp) = 2 and exp[0] == "NOT":
                return "false" if interpret(exp[1], dict) == "true" else "true"
