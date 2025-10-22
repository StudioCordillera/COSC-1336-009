# function returns multiple values
def addMoney(number):
   if (number < 0):
      return "Negative Number"
   elif (number == 0):
      return "Zero"
   else:
      return "Postive Number"

# caller of fucntion
value =  addMoney(-5)
print (value)
