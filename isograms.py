#!/usr/bin/python3
"""
Codewars: Isogram

An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.
"""


def is_isogram(string):
    count = 0
    if string == "":
        return True
    else:
        for i in range(len(string)):
            for x in range(i+1, len(string)):
                if string[i].lower() == string[x].lower():
                    count += 1

    return False if count > 1 else True



print(is_isogram("isIsogram"))



