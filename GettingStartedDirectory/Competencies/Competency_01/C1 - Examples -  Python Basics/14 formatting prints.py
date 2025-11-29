# Name      
# Date      August 27, 2020
# Project#
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# Demonstrate declaring variable and calculation
# ----------------------------------------------------------------

# initialize variables
number1 = 24
number2 = 7

# adds the numbers
answer = number1 / number2

# print  without decimal restriction
print ("My quotient is ", answer)

# print with 4 decimal places
print ("My quotient is ", '% 10.4f' % answer)

# check different formatting print
value = 10.4
print("My quotient is ",'% 6.2f' % value)
print("My quotient is ",'% 12.1f' % value)
print("My quotient is ",'%012.1f' % value)

# using format
print("My quotient is ", format(value, '.03f'))

