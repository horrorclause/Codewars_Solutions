#!/usr/bin/env python3
"""
Codewars: Pete, the Baker

Write a function cakes(), which takes the recipe (object) and
the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer).
For simplicity there are no units for the amounts
"""


def cakes(recipe, available):
    total = []  # Store how many cakes could be made from the specific ingredients
    for k in recipe:    # Checks if recipe key in available
        if k in available:    # If the recipe key is available, divide recipe amount from total available
            total.append((available[k]//recipe[k]))  # Add the amount to total list
        else:
            total.append(0)  # If the recipe key is not available, append 0
    return min(total)   # Return the smallest value b/c this will dictate how many complete cakes can be made


print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))