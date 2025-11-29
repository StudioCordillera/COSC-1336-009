# Name      Ally Baba
# Date      February 7 2020
# Program   Function
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description

def prLines(str, num):
    "Print num lines consisting of str, repeating str once more on each line."
    
    for n in range(0,num):
        print (str * (n + 1))

prLines("\u2665", 5) # is a heart symbol
print('\n')
prLines('* ', 4)
