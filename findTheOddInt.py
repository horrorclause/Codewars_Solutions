#!/usr/bin/env python3
"""
Codewars: Find the Odd Int

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""


def find_it(seq):
    for i in seq:
        temp = seq.count(i)
        if temp % 2:
            return i

