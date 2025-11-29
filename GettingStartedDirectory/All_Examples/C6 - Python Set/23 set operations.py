# Name      Ally Baba
# Date      February 7 2020
# Program   dey
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
print(b)

print(a - b)                              # letters in a but not in b

print(a | b )                             # letters in either a or b

print(a & b )                             # letters in both a and b

print(a ^ b)                              # letters in a or b but not both



