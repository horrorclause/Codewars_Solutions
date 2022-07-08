#!/usr/bin/env python3
"""
Codewars: Dot Calculator

You have to write a calculator that receives strings for input. The dots will represent the number in the equation.
There will be dots on one side, an operator, and dots again after the operator.
The dots and the operator will be separated by one space.

"""

def calculator(txt):
    operators = [
        "+",
        "//",
        "*",
        "-"
    ]

    for i in txt:
        if i and txt[txt.index(i)+1] == "/":
            firstNum = txt.split(" ")[0].count('.')
            secondNum = txt.split(" ")[2].count('.')
            return eval(f'{firstNum}//{secondNum}')*"."
          
        
        elif i in operators:
            firstNum = txt.split(" ")[0].count('.')
            secondNum = txt.split(" ")[2].count('.')
            op = txt.split(" ")[1]
            return eval(f'{firstNum}{op}{secondNum}')*"."
            

#print(calculator(". // .."), calculator(". // ..").count('.'))
