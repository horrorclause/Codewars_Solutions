#!/usr/bin/python3
"""
Codewars: Remove The Minimum

Given an array of integers, remove the smallest value. Do not mutate the original array/list.
If there are multiple elements with the same value, remove the one with a lower index.
If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.
"""


def remove_smallest(numbers):
    if len(numbers) == 0:
        return numbers
    else:
        new = [x for x in numbers]
        new.pop(numbers.index(min(numbers)))
        return new
