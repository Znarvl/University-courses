from calc import *
from copy import deepcopy

def eval_program(calc,var_table = {}):
    """
    Kollar om calc är ett program annars printa error meddelande
    """

    if isprogram(calc):
        var_table = deepcopy(var_table)

        eval_statements(program_statements(calc), var_table)
        return var_table

    else:
        raise ValueError


def eval_statements(calc,var_table):
    """
    Går igenom alla olika fall i calc och letar
    efter vilken funktion den ska kalla på
    """


    if empty_statements(calc):
        return var_table

    eval_statement(first_statement(calc),var_table)

    return eval_statements(rest_statements(calc),var_table)

def eval_statement(calc,var_table):

    """Går igenom och kollar vilket statement calc är och
    kallar på rätt funktion"""


    if empty_statements(calc):
        return var_table

    if isassignment(calc):
        assignment(calc, var_table)

    elif isrepetition((calc)):
        repetition(calc, var_table)

    elif isselection((calc)):
        eval_selection(calc, var_table)

    elif isbinary((calc)):
        binary_exp(calc, var_table)

    elif isinput(calc):
        _input(calc,  var_table)

    elif isoutput((calc)):
        _output(calc, var_table)

    return var_table

def assignment(exp,var_table):
    """
    Sätter en variabel som tas in från exp till ett värde.
    Antingen ett heltal, en annan variabel eller ett utryck
    med flera variabler eller heltal
    """


    try:
        if isbinary(assignment_expression(exp)):
            var_table[assignment_variable(exp)] = binary_exp \
            (assignment_expression(exp),var_table)
        if isconstant(assignment_expression(exp)):
            var_table[assignment_variable(exp)] = assignment_expression(exp)
        if isvariable(assignment_expression(exp)):
            var_table[assignment_variable(exp)] = \
            var_table[assignment_expression(exp)]
        return var_table
    except:
        print("Något gick fel")
        raise KeyError



def var_value(var,var_table):
    """
    Funktion som kollar om var är en variabel
    """


    if isvariable(var):
        return var_table[var]
    elif isbinary(var):
        return binary_exp(var,var_table)
    return var

def repetition(exp,var_table):
    """
    Loopar igenom flera expressions så länge vilkoret gäller
    """


    try:
        if iscondition(repetition_condition(exp)):
            if selection(selection_condition(exp),var_table):
                eval_statements(repetition_statements(exp),var_table)
                repetition(exp,var_table)
        return var_table
    except:
        print("syntaxerror rep")
        raise SyntaxError

def _input(exp,var_table):
    """
    Låter användaren ange ett värde till en variabel
    """

    stringV = "Enter value for "+ input_variable(exp) +": "
    value = input(stringV)
    var_table[input_variable(exp)] = int(value)
    return var_table

def eval_selection(exp,var_table):
    """
    Utför en expression om vilkoret stämmer
    """


    try:
        if selection(condition_operator(exp),var_table):
            eval_statement(selection_true(exp),var_table)
        elif hasfalse(exp):
            eval_statement(selection_false(exp),var_table)

        return var_table
    except:
        print("eval_selection fail")
        raise KeyError
    else:
        print("syntax error eval_sel")
        raise SyntaxError

def selection(exp,var_table):
    """
    Kontrollerar om ett visst vilkor stämmer
    """


    if selection_condition(exp) == ">" and (var_value(condition_left(exp), \
    var_table) > var_value(condition_right(exp),var_table)):
        return True
    if selection_condition(exp) == "<" and (var_value(condition_left(exp), \
    var_table) < var_value(condition_right(exp),var_table)):
        return True
    if selection_condition(exp) == "=" and (var_value(condition_left(exp), \
    var_table) == var_value(condition_right(exp),var_table)):
        return True
    else:
        return False


def _output(exp,var_table):
    """
    Skrivet ur en variabels värde i konsolen
    """


    print(output_variable(exp),'=',var_table[output_variable(exp)])

def binary_exp(exp,var_table):
    """
    Går igenom exp reskursivt,räknar ut alla uttryck och returnar summan
    """
    

    if not(isinstance(binary_left(exp),list)) and not(isinstance \
    (binary_right(exp),list)):
        if binary_operator(exp) == "*":
            return var_value(binary_left(exp),var_table) * var_value \
            (binary_right(exp),var_table)

        elif binary_operator(exp) == "-":
            return var_value(binary_left(exp),var_table) - var_value \
            (binary_right(exp),var_table)

        elif binary_operator(exp) == "+":
            return var_value(binary_left(exp),var_table) + var_value \
            (binary_right(exp),var_table)

        elif binary_operator(exp) == "/":
            return var_value(binary_left(exp),var_table) / var_value \
            (binary_right(exp),var_table)

    if isbinary(condition_left(exp)):
        exp[0] = binary_exp(condition_left(exp),var_table)
        res = binary_exp(exp,var_table)

    if isbinary(condition_right(exp)):
        exp[2] = binary_exp(condition_right(exp),var_table)
        res = binary_exp(exp,var_table)

    return res


calc8 = ['calc',
                ['read', 'x'],
                ['set', 'zero', 0],
                ['set', 'pos', 1],
                ['set', 'nonpos', -1],
                ['if', ['x', '=', 0],
                 [['print', 'zero'], ['set', 'x', 2]]],
                ['if', ['x', '>', 0],
                 ['print', 'pos']],
                ['if', ['x', '<', 0],
                 ['print', 'nonpos']]]
calc7 = ['calc', ['read', 'p1'],
                ['set', 'p2', 47],
                 ['set', 'p3', 179],
                ['set', 'result', [['p1', '*', 'p2'], '-', 'p3']],
                 ['print', 'result']]

calc4 = ['calc',
                ['read', 'n'],
                    ['set', 'sum', 0],
                    ['while', ['n', '>', 0],
                     ['set', 'sum', ['sum', '+', 'n']],
                     ['set', 'n', ['n', '-', 1]]],
                ['print', 'sum']]

calc2 = ['calc',
['set', 'result', [['p1', '/', 'p2'], '-', ['p3', '-' ,['p1', '+', 'p1']]]],
['set','g','p1']]



func = ['calc',['if', [['a', '+', 'b'], '<', 'c'],
				['print', 'output']]]




eval_program(calc8)
