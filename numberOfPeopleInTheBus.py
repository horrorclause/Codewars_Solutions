#!/usr/bin/python3
"""
Codewars: Number of People in the Bus

You are provided with a list (or array) of integer pairs.
Elements of each pair represent number of people get into bus (The first item) and
number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the last bus station (after the last array).
Even though it is the last bus stop, the bus is not empty and some people are still in the bus,
and they are probably sleeping there :D
"""


def number(bus_stops):
    peopleOn = 0
    peopleOff = 0

    for lst in bus_stops:
        peopleOn += lst[0]
        peopleOff += lst[1]

    return peopleOn - peopleOff

print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))