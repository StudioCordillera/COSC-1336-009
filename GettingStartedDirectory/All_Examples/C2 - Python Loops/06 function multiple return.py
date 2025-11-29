# Name      Ally Baba
# Date      February 7 2020
# Program   Function
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description

# function returns multiple values
def AddMoney(number):
   if number < 0:
      return "Negative Number"
   elif number == 0:
      return "Zero"
   else:
      return "Postive Number"

value =  AddMoney(-5)
print (value)
