# Name      
# Date      August 27, 2020
# Project#
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# Demonstrate multi line
# ----------------------------------------------------------------
# Python allows lines to be continued by putting a backslash at the end of
# the first part.

# variable decleration
bill = 2
alice = 3
frank = 1
barney = 1

# calculation
fred = bill + alice + frank - \
       barney

# print section
print( "fred =", fred)
print('\n')  # prints a new line

# The compiler will also combine lines when the line break in contained
# in a grouping pair, such as parens.
joe = 3 * (fred +
        bill - alice)

# print section
print ("joe =", fred)
