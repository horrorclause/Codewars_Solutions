#!/usr/bin/env python3
"""
Codewars: Count by X

Create a function with two arguments that will return an array of the first (n) multiples of (x).

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array
"""

def count_by(x, n):
    num = []
    count = 0
    for i in range(n):
        count += x
        num.append(count)
    return num


