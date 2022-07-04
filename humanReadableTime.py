#!/usr/bin/python3
"""
Codewars: Human Readable Time

Write a function, which takes a non-negative integer (seconds) as input and returns
the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)
"""

import datetime


def make_readable(seconds):

    time = datetime.timedelta(seconds=seconds)
    return f'{time.days * 24 + time.seconds // 3600:02}:{(time.seconds % 3600) // 60:02}:{time.seconds % 60:02}'


