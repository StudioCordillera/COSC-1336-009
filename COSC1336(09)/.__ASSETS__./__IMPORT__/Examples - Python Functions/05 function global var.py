# Name      Ally Baba
# Date      February 7 2020
# Program   Function
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# ...unless declared global.

snoggle = 20

def wangle(n):
    global snoggle
    snoggle = n

print ('B:', snoggle,)
wangle(235)
print ("The value of snoggle is : ",snoggle)
