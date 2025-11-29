########################################
## Matthew Ochoa                   #####
## November 25, 2025               #####
## Project: 04                     #####
## Status: FINISHED                #####
## Class: COSC 1336                #####
########################################

# ------------------------------------------------------------#
#                | Project 3 - Requirements |                 #
# ------------------------------------------------------------#

'''| Objectives | 
    
    Core:
        1) Prompts the user to enter 1 single (input as integer).
        2.1) Calculates - appends odd numbers in range of the provided number as a ceiling into a list, and 1 being a floor. (INCLUSIVE)
            2.2) Calculates a sum from (the list beeing appended to).
        3) Displays the odd numbers from the collection by iterating over a loop, then provides the sum. 
        
'''
###############################################################
##                    PROVIDED FUNCTIONS                     ##
###############################################################

# This function will return an integer input from the user
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')

# This function will return a float input from the user
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value

# This function will return a string input from the user
def getCharData(prompt):

    while (True):
        value = input(prompt)

        value = value.upper()
        if (value in ['W', 'D', 'E']):
            return value

        print('\t\tERROR Message: Wrong selection')


###############################################################
##                      START - MY CODE                      ##
###############################################################

# Display Start of Program Boiler SOPB
#  ------------------------------------------------------------------------
def projectStart():
    print(' ' * 4, '-'* 80, '\n',' ' * 4, 'Start of Project 4')
    print(' ' * 5, 'Written by: Matthew Ochoa')
    print(' ' * 5,'Date: 11/25/2025 ')
    print(' ' * 4,'-' * 80)
    print('\t  Odd numbers and sum of range in input program')
    print(' ' * 4,'-' * 80, '\n')

# Display End of Program Boiler EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print(' ' * 4,'-' * 80, '\n')
    print( ' ' * 5, 'End of Project')
    print(' ' * 4,'-' * 80)


# Store and get input from user while validating and appending
#  ------------------------------------------------------------------------
def storeInput():
    
    print(f'\t  User\'s Entry\n\t','-' * 76)
    
    integerList = []
    
    while True:
        
        intVal = getIntegerData('\t  Enter a positive Integer: ')
        
        if (intVal <=0):
            print('\tNumber must be greater than zero!')
        else:
            break

    for odds in range(1, intVal + 1):
        if (odds%2 != 0):
            integerList.append(odds)
    
    return integerList, intVal

# calculate sum from integerList elements
#  ------------------------------------------------------------------------
def calcSum(integerList):
    
    intSum = sum(integerList)
    
    return intSum

# display the summary of required
#  ------------------------------------------------------------------------
def displaySummary(integerList, intSum, intVal):
    
    print(f'\n\t', '-' * 76, '\n\t  Summary: Sum of Positive Odd Integers\n\t', '-' * 76, '\n\t  Numbers are:\n')
    
    for value in integerList:
        print ('\t\t', value)
        
            
    print(f'\n\t  The sum of odd integers between {1} and {intVal} is {intSum}!')



###############################################################
##    MAIN FUNCTION                                          ##
###############################################################
def main(): 

    # Display SOPB
    projectStart()

    integerList, intVal = storeInput()
    
    intSum = calcSum(integerList)

    displaySummary(integerList, intSum, intVal)

    # Display EOPB
    projectEnd()
      
main() # calling the function main()
