#!/usr/bin/env python3
"""
Codewars: Pete, the Baker

Write a function cakes(), which takes the recipe (object) and
the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer).
For simplicity there are no units for the amounts
"""


def cakes(recipe, available):
    total = []
    for k in recipe:
        if k in available:
            total.append((available[k]//recipe[k]))
        else:
            total.append(0)
    return min(total)


print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))