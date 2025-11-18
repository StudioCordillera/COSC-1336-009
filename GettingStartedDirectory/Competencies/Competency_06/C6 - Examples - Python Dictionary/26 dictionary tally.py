# Name      Ally Baba
# Date      February 7 2020
# Program   dictionary
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# Properties of Dictionary Keys

# More than one entry per key not allowed.
# Which means no duplicate key is allowed.
# When duplicate keys encountered during assignment, the last assignment wins.

dict = {'Name': 1, 'Age': 7, 'Namess': 22}

tally = 0

for i in dict:
    tally = tally + dict[i]

print(tally)
