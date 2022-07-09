#!/usr/bin/env python3
"""
Codewars: Printer Errors
"""
import string

def printer_error(s):
    count = 0
    for i in s:
        if i not in string.ascii_letters[:13]:
            count += 1
    return f"{count}/{len(s)}"



