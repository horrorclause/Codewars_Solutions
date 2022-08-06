#!/usr/bin/env python3

def sum_pairs(ints, s):
    
    new= set()
    for num in ints:
          diff = s - num     
          if diff in new:
              return [diff, num]
          new.add(num)
          
          
print(sum_pairs([10, 5, 2, 3, 7, 5, 6],         10))