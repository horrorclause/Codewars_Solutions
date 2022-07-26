#!/usr/bin/env python3
"""
Anagrams: 
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none
"""

def anagrams(word, words):
    new = [x for x in word] # Splits the string into a list of characters
    matches = [] # Empty list to store potential matches

    for i in words:
        a = [c for c in i] # Splits provided words into list of characters
        new.sort()  # Sorts lists so the words can be compared to check if they are anagrams
        a.sort()
        if new == a:    # If lists match, then it is an anagram and added to the "matches" list
            matches.append(i)
    return matches

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))