# Name      Ally Baba
# Date      February 7 2020
# Program   Function
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# References inside functions are local...

snoggle = 17
def wongle(n):
    snoggle = n

print ('A:', snoggle)
wongle(235)
print ("The value of snoggle is : ", snoggle)
