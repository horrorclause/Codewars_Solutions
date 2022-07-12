#!/usr/bin/env python3
"""
Codewars: Regex Password Validation

You need to write regex that will validate a password to make sure it meets the following criteria:

    At least six characters long
    contains a lowercase letter
    contains an uppercase letter
    contains a number

Valid passwords will only be alphanumeric characters.


At least one uppercase English letter. You can remove this condition by removing (?=.*[A-Z])
At least one lowercase English letter.  You can remove this condition by removing (?=.*[a-z])
At least one digit. You can remove this condition by removing (?=.*\d)
[^\W] matches non alphanumeric characters

.* = This matches zero or more occurrences of any character. In other words,
     it essentially matches any character sequence up to a line break.

"""
import re

password =[
    "dYBf5FsJ@#__^cexme",
    "fjd3IR9",
    "DHSJdhjsU",
    "fjd3  IR9",
    "ABC123abc",
    "dsF43",
    "djI38D55",
]

for i in password:
    x = re.search("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[^\W]{6,}$", i)
    print(x)