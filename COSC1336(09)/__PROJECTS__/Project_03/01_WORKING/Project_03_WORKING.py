########################################
## Matthew Ochoa                   #####
## November 06, 2025               #####
## Project: 03                     #####
## Status: FINISHED                #####
## Class: COSC 1336                #####
###############################################################
## Project 3 Objectives | Input > Calc (Handling) > Summary  ##
###############################################################

# This function will return an integer input from the user
def getIntegerData(prompt):
    value = int(input(prompt))
    return value

# This function will return a float input from the user
def getFloatData(prompt):
    value = float(input(prompt))
    return value

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value

###############################################################
##    My Code Below                                          ##
###############################################################

# Display Start of Program Boiler SOPB
#  ------------------------------------------------------------------------
def projectStart():

    print('Start of Project 3')
    print('Written by: Matthew Ochoa')
    print('Date: 11/06/2025\n')
    print('-' * 50 + '\n')
    print('\tBank Fees Calculator')
    print('-' * 50 + '\n')
    print('\t', '-' * 50 + '\n')
    print('\tBank Teller\'s Entry')
    print('\t', '-' * 50 + '\n')

# Display End of Program Boiler EOPB
#  ------------------------------------------------------------------------
def projectEnd():

    print('End of Project 3')
    print('-' * 50 + '\n')

# Calculate Fees Function
#  ------------------------------------------------------------------------
def calculateFees(checks):

    # Debug
    # print('Debug: Calculating Checks')

    if (checks < 20):

        # Checks were Less than or equal to 20
        checkRange = 'less than 20'

        # Calc Fees
        fees = checks * .1
        
        # Debug
        # print('Debug: checks was less 20')

    elif (checks < 40):

        # Checks were between 20 - 39
        checkRange = 'between 20 - 39'

        # Calc Fees
        fees = checks * .08

        # Debug
        # print('Debug: checks was less than 40')

    elif (checks < 60):

        # Checks were between 40 - 59
        checkRange = 'between 40 - 59'

        # Calc Fees
        fees = checks * .06

        # Debug
        # print('Debug: checks was less than 60')

    else:

        # Checks were more greater than or equal to 60
        checkRange = '60 or more'

        # Calc Fees
        fees = checks * .04

        # Debug
        # print('Debug: checks was greater than or equal to 60')

    return fees, checkRange

# Handle Shenanigans (user enters negative integer) Function
# & Get / Return checks input
#  ------------------------------------------------------------------------
def shenanigans():

    # Debug
    # print('Debug: Searching for shenanigans... ')

    checks = 0 # For Debug error prevention

    while (True):

        # Debug
        # print('Debug: While loop initiated')

        # Handle non-integer input data-types
        try:
            
            # Debug
            # # print('Debug: Trying for Valid input data-types')

            checks = getIntegerData('\tEnter the number of checks written this month? ')

        except ValueError:

            # Debug
            # print('Debug: User entered a non Integer Value')

            print('\tOnly Whole Numbers Dumb Dumb!!... ')
        
        # Debug
        # print('Debug: checks = ', checks)

        # Is checks a positive integer?
        if (checks <= 0):

            # Debug
            # print('Debug: Checks was not greater than equal to 0')

            print('\tQuit your shenanigans!')

        else:

            # Debug 
            # print('Debug: Checks was equal or geater than 0')
            # print('Debug: No Shenanigans Detected!... ')

            break

    return checks

# Display Fees Summary
#  ------------------------------------------------------------------------
def displayFees(month, checks, fees, checkRange):

    # Debug
    # print('Debug: displayFees func')

    # Display Summary
    print('\n\t', '-' * 50)
    print('\tSummer: Bank')
    print('\t', '-' * 50)
    print('\tMonth of statement: ', month)
    print('\tFor writing ', checks, 'checks, the bank fee is $', fees, 'since it fell within the ', checkRange, 'number range.\n')
    print('\t', '-' * 50, '\n')

###############################################################
##    MAIN FUNCTION                                          ##
###############################################################
def main(): 

    # Debug
    # print('Debug: main func')

    # Display SOPB
    projectStart()

    # Prompt user for month
    month = getStringData('\tEnter the month: ')

    # Debug
    # print('Debug: Month = ', month)

    # Get checks input then Handle Shenanigans
    checks = shenanigans()

    # Debug
    # print('Debug: Checks = ', checks)

    # Calculate fees per number range steps
    fees, checkRange = calculateFees(checks)

    # Debug
    # print('Debug: Fees = ', fees)

    # Display Monthly Fees
    displayFees(month, checks, fees, checkRange)

    # Debug
    # print('Debug: Month = ', month)
    # print('Debug: Checks = ', checks)
    # print('Debug: Fees = ', fees)

    # Display EOPB
    projectEnd()
      
main() # calling the function main()