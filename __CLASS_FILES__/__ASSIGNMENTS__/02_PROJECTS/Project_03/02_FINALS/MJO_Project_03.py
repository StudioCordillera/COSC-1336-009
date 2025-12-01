###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   November 6, 2025    |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|   REQUIREMENTS - Project 03                                |
|   Objectives: Bank Monthly Fee Calculator                  |
|____________________________________________________________|

INPUTS (User Provided):
    - Month of statement (string - name or number)
      * Accepts: "JAN", "January", "1", etc.
    - Number of checks written (integer, must be positive)

PROCESSING:
    - Validate month input (accept names, abbreviations, numbers)
    - Validate check count is positive integer
    - Calculate flat monthly fee: $10 × month number (1-12)
    - Calculate per-check fee based on volume:
      * < 20 checks: $0.10 per check
      * 20-39 checks: $0.08 per check
      * 40-59 checks: $0.06 per check
      * ≥ 60 checks: $0.04 per check
    - Calculate total fees: flat fee + per-check fees

DISPLAY:
    - Month of statement
    - Number of checks written
    - Total bank fees for the month

FUNCTIONS:
    - projectStart(): Display program header
    - projectEnd(): Display program completion message
    - getIntegerData(prompt): Get validated integer input
    - getFloatData(prompt): Get validated float input
    - getStringData(prompt): Get and format string input
    - getUserInput(): Coordinate user input collection
    - shenanigans(): Validate inputs and handle errors
    - monthHandler(month): Parse and validate month input
    - calculateFees(monthIndex, checks): Calculate total fees
    - printSummary(): Display fee calculation results
    - main(): Program orchestration

VALIDATION RULES:
    - Month must be valid (1-12 or valid name/abbreviation)
    - Check count must be positive integer
    - Invalid input triggers error messages and re-prompts

FEE STRUCTURE:
    - Flat fee: $10 × month number
    - Volume-based per-check fees (tiered pricing)

______________________________________________________________
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


#   Get Integer Input with Validation
#  ------------------------------------------------------------------------
def getIntegerData(prompt):
    try:
        value = int(input(prompt))  # Get integer from user <
    except ValueError:
        print('\tONLY INTEGERS!!')
    return value  # Return to caller >



#   Get Float Input with Validation
#  ------------------------------------------------------------------------
def getFloatData(prompt):
    try:
        value = float(input(prompt))  # Get float from user <
    except ValueError:
        print('\tONLY NUMBERS!!')
    return value  # Return to caller >


#   Get String Input with Formatting
#  ------------------------------------------------------------------------
def getStringData(prompt):
    value = input(prompt).strip().lower().upper()  # Get and format string <
    return value  # Return to caller >


#   SOPB
#  ------------------------------------------------------------------------
def projectStart():
    print('-' * 50 + '\n')
    print('Start of Project 3')
    print('Written by: Matthew Ochoa')
    print('Date: 11/06/2025\n')
    print('-' * 50 + '\n')
    print('\tBank Teller\'s Entry')
    print('\t', '-' * 50 + '\n')


#   EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print('\tEnd of Project 3')
    print('-' * 50 + '\n')


#   Calculate Bank Fees
#  ------------------------------------------------------------------------
def calculateFees(monthIndex, checks):
    # Determine per-check fee based on volume tiers
    if (checks <20):
        bankFees = float(checks * .10)   # < 20: $0.10/check |
    elif(checks <40):
        bankFees = float(checks * .08)   # 20-39: $0.08/check |
    elif(checks<60):
        bankFees = float(checks * .06)   # 40-59: $0.06/check |
    else:
        bankFees = float(checks * .04)   # ≥ 60: $0.04/check |
    
    # Calculate flat monthly fee based on month number
    flatFees = float(10 * monthIndex)  # $10 × month number |
    
    # Calculate total fees
    totalFees = flatFees + bankFees  # Sum both fee types |
    
    return totalFees  # Return total >

#   Coordinate User Input Collection
#  ------------------------------------------------------------------------
def getUserInput():
    # Delegate to validation function
    month, checks, monthIndex = shenanigans()  # <
    
    return month, checks, monthIndex  # Return validated data >

#   Validate All User Inputs
#  ------------------------------------------------------------------------
def shenanigans():
    # Validate month input with error handling
    while True:
        try:
            month, monthIndex = monthHandler(getStringData('\tEnter the month: '))  # <
        except IndexError:
            print('\tENTER A MONTH')
        break
    
    # Validate check count is positive
    while True:
        checks = getIntegerData('\tEnter the number of checks written this month? ')  # <
        if checks >0:
            break  # Valid input |
        else: 
            print('\tONLY POSITIVE INTEGERS!!')  # Error message >
    
    return month, checks, monthIndex  # Return validated inputs >
    
    
#   Parse and Validate Month Input
#  ------------------------------------------------------------------------
def monthHandler(month):
    # Month dictionary: number → [abbreviation, full name]
    monthList = {
        1: ['JAN', 'JANUARY'],
        2: ['FEB', 'FEBUARY'],
        3: ['MAR', 'MARCH'],
        4: ['APR', 'APRIL'],
        5: ['MAY', 'MAY'],
        6: ['JU7', 'JUNE'],
        7: ['JUL', 'JULY'],
        8: ['AUG', 'AUGUST'],
        9: ['SEP', 'SEPTEMBER','SEPT',],
        10: ['OCT', 'OCTOBER'],
        11: ['NOV', 'NOVEMBER'],
        12: ['DEC', 'DECEMBER']
    }
    
    # Handle numeric month input
    if (month.isnumeric() == True):
        try: 
            month = int(month)  # Convert to integer |
        except ValueError:
            print('\tCHOOSE 01 OR Jan OR January FORMAT!!')
        
        if month in monthList:
            try:
                monthKey = monthList[month][1]   # Get full name |
                monthValue = month                # Store number |
                return monthKey, monthValue  # Return both >
            except:
                print('\tINCORRECT FORMATTING')
        else:
            print('\tMUST BE A VALID MONTH AND FORMAT!!')
    
    # Handle text month input (name or abbreviation)
    else:
        for keys in monthList:
            if month in monthList[keys]:
                monthKey = monthList[keys][1]   # Get full name |
                monthValue = keys                # Get number |
                return monthKey, monthValue  # Return both >
            
            
#   Display Fee Calculation Summary
#  ------------------------------------------------------------------------
def printSummary(month, checks, totalFees):
    print('\n\t', '-' * 50)
    print('\tSummary: Bank')
    print('\t', '-' * 50)
    print(f'\tMonth of statement: {month}')
    print(f'\tFor writing {checks} checks, the bank fee is ${totalFees:.2f}.\n')
    print('\t', '-' * 50, '\n')
    

#   MAIN FUNCTION - Program Orchestration
#  ------------------------------------------------------------------------
def main(): 
    # Display program start
    projectStart()
    
    # Get validated user input
    month, checks, monthIndex = getUserInput()  # <
    
    # Calculate bank fees
    totalFees = calculateFees(monthIndex, checks)  # <
    
    # Display fee summary
    printSummary(month, checks, totalFees)  # >
    
    # Display program end
    projectEnd()


#   PROGRAM ENTRY POINT
#  ------------------------------------------------------------------------
main()