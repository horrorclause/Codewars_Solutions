#! /usr/bin/env python3

"""
    Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules.
    You will always be given an array with five six-sided dice values.
    A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points,
    but not both in the same roll.
"""



def score(dice):
    
    points = {
        1: 1000,
        2: 200,
        3: 300,
        4: 400,
        5: 500,
        6: 600
    }
    
    singlePoints = {
        1: 100,
        5: 50
    }
    
    counts = {}
    score = 0
    
    # Creating Unique List of numbers, so no duplicates are counted
    for i in dice:
        if i not in counts:
            counts[i] = dice.count(i)
            
    for k in counts:
        if k not in singlePoints and counts[k] >= 3: # Any number other than 1 or 5, that has a count > 3
            score += points[k]
        elif k in singlePoints and counts[k] >= 3: #  1 or 5, that has a count > 3 will be scored as 3 pointer plus the individual points
            score += points[k]
            score += ((counts[k]-3)*singlePoints[k])                    
        elif k in singlePoints and (0 < counts[k] < 3): #  1 or 5, that has a count less than 3 but greater than 0 will be scored at that number times individual score.
            score += (counts[k] * singlePoints[k])

print(score([4, 4, 4, 4, 2]))
            

