###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   November 25, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|   REQUIREMENTS - Project 04                                |
|   Objectives: Odd Numbers Sum Calculator                   |
|____________________________________________________________|

INPUTS (User Provided):
    - Positive integer (ceiling value, must be > 0)

PROCESSING:
    - Validate input is positive integer
    - Generate list of all odd numbers from 1 to input (inclusive)
    - Calculate sum of all odd numbers in the list

DISPLAY:
    - List all odd numbers (one per line)
    - Display sum of all odd numbers
    - Show range (1 to input value)

FUNCTIONS:
    - projectStart(): Display program header
    - projectEnd(): Display program completion message
    - getIntegerData(prompt): Get validated integer input
    - getFloatData(prompt): Get validated float input
    - getStringData(prompt): Get string input
    - getCharData(prompt): Get validated character input
    - storeInput(): Collect and validate user input, build odd number list
    - calcSum(integerList): Calculate sum of list elements
    - displaySummary(): Display odd numbers and their sum
    - main(): Program orchestration

VALIDATION RULES:
    - Input must be positive integer (> 0)
    - Re-prompt if invalid input provided

ALGORITHM:
    - Range: 1 to user_input (inclusive)
    - Filter: Only odd numbers (num % 2 != 0)
    - Store in list, then calculate sum

______________________________________________________________
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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

#   SOPB
#  ------------------------------------------------------------------------
def projectStart():
    print(' ' * 4, '-'* 80, '\n',' ' * 4, 'Start of Project 4')
    print(' ' * 5, 'Written by: Matthew Ochoa')
    print(' ' * 5,'Date: 11/25/2025 ')
    print(' ' * 4,'-' * 80)
    print('\t  Odd numbers and sum of range in input program')
    print(' ' * 4,'-' * 80, '\n')


#   EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print(' ' * 4,'-' * 80, '\n')
    print( ' ' * 5, 'End of Project')
    print(' ' * 4,'-' * 80)


#   Collect Input and Build Odd Number List
#  ------------------------------------------------------------------------
def storeInput():
    # Display input section header
    print(f'\t  User\'s Entry\n\t','-' * 76)
    
    integerList = []  # Initialize list for odd numbers |
    
    # Validate input is positive
    while True:
        intVal = getIntegerData('\t  Enter a positive Integer: ')  # <
        
        if (intVal <=0):
            print('\tNumber must be greater than zero!')  # Error message >
        else:
            break  # Valid input |
    
    # Build list of odd numbers in range [1, intVal]
    for odds in range(1, intVal + 1):
        if (odds%2 != 0):  # Check if odd |
            integerList.append(odds)  # Add to list |
    
    return integerList, intVal  # Return list and ceiling value >

#   Calculate Sum of List
#  ------------------------------------------------------------------------
def calcSum(integerList):
    intSum = sum(integerList)  # Sum all elements |
    return intSum  # Return total >


#   Display Odd Numbers and Sum
#  ------------------------------------------------------------------------
def displaySummary(integerList, intSum, intVal):
    # Display summary header
    print(f'\n\t', '-' * 76, '\n\t  Summary: Sum of Positive Odd Integers\n\t', '-' * 76, '\n\t  Numbers are:\n')
    
    # Display each odd number
    for value in integerList:
        print ('\t\t', value)  # Print odd number >
    
    # Display final sum
    print(f'\n\t  The sum of odd integers between {1} and {intVal} is {intSum}!')  # >



#   MAIN FUNCTION - Program Orchestration
#  ------------------------------------------------------------------------
def main(): 
    # Display program start
    projectStart()
    
    # Get input and build odd number list
    integerList, intVal = storeInput()  # <
    
    # Calculate sum of odd numbers
    intSum = calcSum(integerList)  # <
    
    # Display results
    displaySummary(integerList, intSum, intVal)  # >
    
    # Display program end
    projectEnd()


#   PROGRAM ENTRY POINT
#  ------------------------------------------------------------------------
main()
